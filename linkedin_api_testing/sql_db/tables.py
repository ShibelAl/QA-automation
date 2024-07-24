import sqlite3
from infra.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.models.company_jobs import CompanyJobs
from logic.company import Company


class Tables:
    """
    A class to manage database operations for LinkedIn jobs data.
    """

    def __init__(self, db_name='linkedin.db'):
        """
        Initialize the Tables class.

        Args:
            db_name (str): The name of the SQLite database file. Default is 'linkedin.db'.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._config = ConfigProvider.load_config_json()
        self._api_request = APIWrapper()

    def get_response(self):
        """
        Fetch job data from the API.

        Returns:
            dict: The JSON response from the API containing job data.
        """
        self._config = ConfigProvider.load_config_json()
        self._api_request = APIWrapper()
        payload = self._config['get_company_jobs_payload']
        company_ids = payload['companyIds']
        page = payload['page']
        company_object = CompanyJobs(company_ids, page)
        response = Company(self._api_request).get_company_job_by_body(company_object.to_dict())
        response_body = response.json()
        # Uncomment the next line to print the response body
        # print(response_body)
        return response_body

    def create_companies_table(self):
        """
        Create the companies table in the database if it doesn't already exist.
        """
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS companies (
            name VARCHAR(255) PRIMARY KEY,
            url TEXT
        );
        ''')

    def create_jobs_table(self):
        """
        Create the jobs table in the database if it doesn't already exist.
        """
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            job_id VARCHAR(255) PRIMARY KEY,
            title VARCHAR(255),
            company_name VARCHAR(255),
            FOREIGN KEY (company_name) REFERENCES companies(name)
        );
        ''')

    def clear_tables(self):
        """
        Clear all records from the jobs and companies tables.
        """
        self.cursor.execute("DELETE FROM jobs")
        self.cursor.execute("DELETE FROM companies")
        self.conn.commit()

    def insert_jobs_records(self):
        """
        Insert job records into the database.

        Fetches job data from the API, clears existing tables, creates tables if they don't exist,
        and inserts job records into the jobs table. If a record already exists, it will be replaced.
        """
        try:
            self.clear_tables()
        except sqlite3.OperationalError as e:
            print(f"No such table to clear!: {e}")

        self.create_companies_table()
        self.create_jobs_table()
        items = self.get_response()['data']['items']
        for item in items:
            job_id = item['id']
            title = item['title']
            company_name = item['company']['name']
            try:
                self.cursor.execute("INSERT OR REPLACE INTO jobs (job_id, title, company_name) VALUES (?, ?, ?)",
                                    (job_id, title, company_name))
                self.conn.commit()
            except sqlite3.IntegrityError as e:
                print(f"Error inserting job record: {e}")

    def drop_table(self):
        """
        Drop the jobs and companies tables from the database.
        """
        self.cursor.execute("DROP TABLE IF EXISTS jobs")
        self.cursor.execute("DROP TABLE IF EXISTS companies")
        self.conn.commit()

    def close_connection(self):
        """
        Close the database connection.
        """
        self.conn.close()


if __name__ == "__main__":
    tables = Tables()
    tables.get_response()
    tables.insert_jobs_records()
    tables.close_connection()
