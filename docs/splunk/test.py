import requests
import json

## 기능
# 1. nvd api 조회 및 데이터 저장
# ** CVE 기본 정보 **
# - CVE ID: CVE 번호 (예: CVE-2024-6387)
# - 상태: 취약점의 현재 상태 (예: Awaiting Analysis, Modified, Rejected)
# - 발행일: 취약점이 처음 게시된 날짜
# - 최종 수정일: 마지막으로 수정된 날짜
# - 출처: CVE의 출처 (예: Red Hat, Wordfence 등)

# ** 취약점 설명 **
# - 설명: 취약점에 대한 설명 (여러 언어로 지원 가능)
# - 취약점 유형: 취약점 분류 (예: Stored XSS, RCE)
# - 관련 CWE (Common Weakness Enumeration): 취약점의 CWE 번호 및 설명
# - 3. CVSS (Common Vulnerability Scoring System) 점수 및 세부 정보
# - 기본 점수: CVSS 기본 점수와 등급 (예: 8.1 HIGH)
# - CVSS 벡터: 공격의 특성 요약 (예: CVSS:3.1/AV
# - 공격 벡터, 복잡성, 권한 요구사항, 사용자 상호작용 등 상세 항목
# - Exploitability Score 및 Impact Score: 각각의 점수와 취약점 영향

#  ** 취약 소프트웨어 (Affected Software) **
# - CPE (Common Platform Enumeration): 취약점에 영향받는 소프트웨어 및 버전 정보 (예: cpe:2.3:a:openbsd:openssh:7.6)
# - 버전 정보: 해당 버전 범위 (예: 4.0 이상 8.6 미만)

#  ** 레퍼런스 및 외부 링크 **
# - 공식 문서 링크: 관련 패치나 보안 공지 (예: Red Hat Errata)
# - 블로그 및 보고서: 상세한 분석이 포함된 외부 블로그, 보안 보고서
# - 익스플로잇 정보: PoC, 익스플로잇 코드가 있는 경우 링크


# 2. snort org 또는 ET rule 확인 후, 있으면 출력

# --------------------------------------------------------------

# 고정 매개변수
nvd_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
api_key = "a07b3e02-69c0-44af-ae58-52214fde29dc"

def user_input():
    print("Please enter the NVD CVE number.")
    user_data = input("Example(CVE-2024-1234) : ")
    return user_data

def nvd_api(cve):
    search_url = nvd_url + "?cveId=" + cve
    headers = {
        "api_key": api_key
    }

    response = requests.get(search_url, headers=headers)
    nvd_data = response.text
    print(nvd_data)
    
    json_data = json.loads(nvd_data)
    return json_data

# def parse_vulnerability_data(json_data):
#     for vulnerability in json_data.get("vulnerabilities", []):
#         cve_info = vulnerability.get("cve", {})

#         # CVE 기본 정보
#         cve_id = cve_info.get("id")
#         published = cve_info.get("published")
#         last_modified = cve_info.get("lastModified")
        
#         # Descriptions 정보
#         descriptions = [
#             desc.get("value") for desc in cve_info.get("descriptions", []) if desc.get("lang") == "en"
#         ]
        
#         # Metrics 정보 (여러 source가 있을 수 있음)
#         metrics_info = []
#         for metric in cve_info.get("metrics", {}).get("cvssMetricV31", []):
#             metric_data = {
#                 "version": metric.get("cvssData", {}).get("version"),
#                 "vectorString": metric.get("cvssData", {}).get("vectorString"),
#                 "source": metric.get("source"),
#                 "baseScore": metric.get("cvssData", {}).get("baseScore"),
#                 "baseSeverity": metric.get("cvssData", {}).get("baseSeverity")
#             }
#             metrics_info.append(metric_data)

#         # Weaknesses 정보 (여러 source가 있을 수 있음)
#         weaknesses_info = []
#         for weakness in cve_info.get("weaknesses", []):
#             weaknesses_data = {
#                 "source": weakness.get("source"),
#                 "description": [desc.get("value") for desc in weakness.get("description", [])]
#             }
#             weaknesses_info.append(weaknesses_data)

#         # 출력
#         print(f"CVE ID: {cve_id}")
#         print(f"Published Date: {published}")
#         print(f"Last Modified Date: {last_modified}")
#         print(f"Descriptions: {descriptions}")
        
#         print("\nMetrics Info:")
#         for metric in metrics_info:
#             print(f"  - Version: {metric['version']}")
#             print(f"    Vector String: {metric['vectorString']}")
#             print(f"    Source: {metric['source']}")
#             print(f"    Base Score: {metric['baseScore']}")
#             print(f"    Base Severity: {metric['baseSeverity']}")
        
#         print("\nWeaknesses Info:")
#         for weakness in weaknesses_info:
#             print(f"  - Source: {weakness['source']}")
#             for description in weakness["description"]:
#                 print(f"    Description: {description}")

#         print("\n" + "="*50 + "\n")

def main():
    cve_num = user_input()
    nvd_data = nvd_api(cve_num)
    # parse_vulnerability_data(nvd_data)
    return

if __name__ == "__main__":
    main()
