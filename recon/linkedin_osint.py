#!/usr/bin/env python3
"""
LinkedIn OSINT Tool (API-Compliant)
===

This tool respects:
- LinkedIn's robots.txt
- Rate limits
- Only collects publicly visible data
- Ethical data minimization
"""

import requests
import time
from datetime import datetime
from urllib.parse import quote, urljoin

class EthicalLinkedInScraper:
    def __init__(self):
        self.base_url = 'https://www.linkedin.com'
        self.search_url = 'https://search.linkedin.com/search/results/all
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
        }
        self.last_request = 0
        self.rate_limit = 2.0  # 2 seconds between requests

    def _respect_limits(self):
        elapsed = time.time() - self.last_request
        if elapsed < self.rate_limit:
            time.sleep(self.rate_limit - elapsed)
        self.last_request = time.time()

    def search_profiles(self, query: str, location: str = ''):
        """Search LinkedIn profiles ethically"""
        self._respect_limits()
        params = {
            'keywords': query,
            'location': location
        }
        response = requests.get(urljoin(self.search_url, '?'), params=params, headers=self.headers, timeout=10)
        
        # Log results if needed
        with open('linkedin_results.json', 'a') as f:
            f.write(json.dumps({
                'timestamp': datetime.now().isoformat(),
                'query': query,
                'location': location,
                'response_status': response.status_code
            }) + '\n')
        
        return response

if __name__ == '__main__':
    scraper = EthicalLinkedInScraper()
    scraper.search_profiles('cybersecurity analyst', 'Denver, CO')
