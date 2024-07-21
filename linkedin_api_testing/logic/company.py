from infra.config_provider import ConfigProvider


class Company:
    def __init__(self, request):
        self._request = request
        self._config = ConfigProvider().load_config_json()

    def get_company_job_by_body(self, comp_job):
        url = f"{self._config['base_url']}/{self._config['get_company_jobs_endpoint']}"
        return self._request.post_request(url, self._config['get_company_jobs_headers'], comp_job)
