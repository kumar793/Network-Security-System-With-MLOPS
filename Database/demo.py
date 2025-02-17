import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import whois
import datetime

def get_features(url):
    features = {}
    
    # Feature 1: having_IP_Address
    features['having_IP_Address'] = 1 if re.match(r'http[s]?://\\d+\\.\\d+\\.\\d+\\.\\d+', url) else 0
    
    # Feature 2: URL_Length
    features['URL_Length'] = len(url)
    
    # Feature 3: Shortining_Service
    shortening_services = ["bit.ly", "goo.gl", "shorte.st", "go2l.ink", "x.co", "ow.ly", "t.co", "tinyurl.com", "tr.im", "is.gd"]
    features['Shortining_Service'] = 1 if any(service in url for service in shortening_services) else 0
    
    # Feature 4: having_At_Symbol
    features['having_At_Symbol'] = 1 if '@' in url else 0
    
    # Feature 5: double_slash_redirecting
    features['double_slash_redirecting'] = 1 if '//' in url[7:] else 0
    
    # Feature 6: Prefix_Suffix
    features['Prefix_Suffix'] = 1 if '-' in urlparse(url).netloc else 0
    
    # Feature 7: having_Sub_Domain
    domain = urlparse(url).netloc
    if domain.count('.') == 1:
        features['having_Sub_Domain'] = 0
    elif domain.count('.') == 2:
        features['having_Sub_Domain'] = 1
    else:
        features['having_Sub_Domain'] = 2
    
    # Feature 8: SSLfinal_State
    try:
        response = requests.get(url, timeout=5)
        if response.url.startswith('https://'):
            features['SSLfinal_State'] = 1
        else:
            features['SSLfinal_State'] = 0
    except:
        features['SSLfinal_State'] = -1
    
    # Feature 9: Domain_registeration_length
    try:
        domain_info = whois.whois(domain)
        expiration_date = domain_info.expiration_date
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]
        registration_length = (expiration_date - datetime.datetime.now()).days
        features['Domain_registeration_length'] = registration_length
    except:
        features['Domain_registeration_length'] = -1
    
    # Feature 10: Favicon
    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        icon_link = soup.find("link", rel="shortcut icon")
        if icon_link:
            features['Favicon'] = 1 if urlparse(icon_link['href']).netloc == domain else 0
        else:
            features['Favicon'] = -1
    except:
        features['Favicon'] = -1
    
    # Feature 11: port
    features['port'] = urlparse(url).port or (443 if response.url.startswith('https://') else 80)
    
    # Feature 12: HTTPS_token
    features['HTTPS_token'] = 1 if 'https-' in domain else 0
    
    # Feature 13: Request_URL
    try:
        total_links = len(soup.find_all('img')) + len(soup.find_all('audio')) + len(soup.find_all('embed')) + len(soup.find_all('iframe'))
        external_links = sum(1 for link in soup.find_all(['img', 'audio', 'embed', 'iframe']) if urlparse(link.get('src')).netloc != domain)
        features['Request_URL'] = external_links / total_links if total_links > 0 else -1
    except:
        features['Request_URL'] = -1
    
    # Feature 14: URL_of_Anchor
    try:
        total_anchors = len(soup.find_all('a'))
        external_anchors = sum(1 for anchor in soup.find_all('a') if urlparse(anchor.get('href')).netloc != domain)
        features['URL_of_Anchor'] = external_anchors / total_anchors if total_anchors > 0 else -1
    except:
        features['URL_of_Anchor'] = -1
    
    # Feature 15: Links_in_tags
    try:
        total_tags = len(soup.find_all(['link', 'script']))
        external_tags = sum(1 for tag in soup.find_all(['link', 'script']) if urlparse(tag.get('href')).netloc != domain)
        features['Links_in_tags'] = external_tags / total_tags if total_tags > 0 else -1
    except:
        features['Links_in_tags'] = -1
    
    # Feature 16: SFH (Server Form Handler)
    try:
        forms = soup.find_all('form')
        empty_forms, external_forms, internal_forms = 0, 0, 0
        
        for form in forms:
            action_url = form.get('action')
            if not action_url or action_url == '':
                empty_forms += 1
            elif urlparse(action_url).netloc != domain and not action_url.startswith('/'):
                external_forms += 1
            else:
                internal_forms += 1
        
        total_forms = len(forms)
        
        if total_forms > 0:
            sfh_ratio = (empty_forms + external_forms) / total_forms
            features['SFH'] = sfh_ratio
        else:
            features['SFH'] = -1
            
    except Exception as e:
        print(f"Error processing SFH feature: {e}")
        features['SFH'] = -1

    
    # Feature 17: Submitting_to_email
    try:
        forms_with_email_action = sum(1 for form in soup.find_all('form') if 'mailto:' in form.get('action', ''))
        features['Submitting_to_email'] = forms_with_email_action / len(soup.find_all('form')) if len(soup.find_all('form')) > 0 else -1
    except Exception as e:
        print(f"Error processing Submitting_to_email feature: {e}")
        features['Submitting_to_email'] = -1

    
    # Feature 18: Abnormal_URL
    try:
        whois_domain_info = whois.whois(domain)
        abnormal_url_flagged_domains_listed_in_whois_db_as_none_or_empty_string_or_not_matching_domain_name_in_urlparse_netloc_function_output_listed_as_abnormal_urls_flagged_as_True_or_False_based_on_this_condition
    except:
        features['Abnormal_URL'] = -1
    
    # Feature 19: Redirect
    features['Redirect'] = len(response.history)
    
    # Feature 20: on_mouseover
    try:
        features['on_mouseover'] = 1 if "onmouseover" in response.text else 0
    except:
        features['on_mouseover'] = -1
    
    # Feature 21: RightClick
    try:
        features['RightClick'] = 1 if "event.button==2" in response.text else 0
    except:
        features['RightClick'] = -1
    
    # Feature 22: popUpWidnow
    try:
        features['popUpWidnow'] = 1 if "alert(" in response.text else 0
    except:
        features['popUpWidnow'] = -1
    
    # Feature 23: Iframe
    try:
        features['Iframe'] = 1 if "<iframe" in response.text else 0
    except:
        features['Iframe'] = -1
    
    # Feature 24: age_of_domain
    try:
        creation_date = domain_info.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        age_of_domain = (datetime.datetime.now() - creation_date).days
        features['age_of_domain'] = age_of_domain
    except:
        features['age_of_domain'] = -1
    
    # Feature 25: DNSRecord
    try:
        features['DNSRecord'] = 1 if domain_info else 0
    except:
        features['DNSRecord'] = -1
    
    # Feature 26: web_traffic
    # This feature typically requires access to external services like Alexa or SimilarWeb
    features['web_traffic'] = -1  # Placeholder
    
    # Feature 27: Page_Rank
    # This feature typically requires access to external services like Google PageRank API
    features['Page_Rank'] = -1  # Placeholder
    
    # Feature 28: Google_Index
    try:
        google_search = requests.get(f"https://www.google.com/search?q=site:{domain}")
        features['Google_Index'] = 1 if "did not match any documents" not in google_search.text else 0
    except:
        features['Google_Index'] = -1
    
    # Feature 29: Links_pointing_to_page
    # This feature typically requires access to external services like Ahrefs or Moz
    features['Links_pointing_to_page'] = -1  # Placeholder
    
    # Feature 30: Statistical_report
    # This feature typically requires access to external services or databases
    features['Statistical_report'] = -1  # Placeholder
    
    return features

# Example usage
url = "http://example.com"
features = get_features(url)
print(features)