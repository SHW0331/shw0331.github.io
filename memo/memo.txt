## pcre 분석

/^(?:는 정규 표현식에서 특정 패턴을 정의하는 데 사용되는 구문입니다. 각각의 의미는 다음과 같습니다:

^: 문자열의 시작을 의미.
(?:...): 캡처하지 않는 그룹(Non-capturing group)입니다. 이 그룹 안에 있는 패턴들이 OR 조건으로 묶이지만, 캡처되지 않습니다. 즉, 해당 그룹 내의 패턴들 중 하나와 일치하면 매칭되지만, 결과로 캡처되지는 않습니다.

이 정규 표현식은 URI의 시작 부분에서 TestService, view, showDateTime, main, 또는 forgotPassword 중 하나로 시작하는지를 확인하는 데 사용됩니다.

# http 함수 뒤에 붙는 경우, 앞에 contet의 부가 함수
content~ pcre http~
# pcre 앞에 http 가 붙는 경우, content의 부가함 수가 아닌, pcre 문자열만을 탐지
http~ pcre


## Snort rule Frame
	
alert tcp any any -> any any (
    msg:"[ET]24-04-D-Link NAS devices Backdoor Account Access and Command Injection Attempt";
    flow:established,to_server;
    content:"GET";
    http_method;
    content:"|2F|cgi|2D|bin|2F|nas|5F|sharing|2E|cgi|3F|";
    http_uri;
    depth:25;
    content:"user|3D|messagebus";
    http_uri;
    fast_pattern;
    content:"passwd|3D|";
    http_uri;
    content:"cmd|3D|15";
    http_uri;
    content:"system|3D|";
    http_uri;
    reference:cve,2024-3273;
    classtype:attempted-admin;
    priority:1;
    sid:24041102;
    rev:1;
)
​

alert http any any -> $HOME_NET any (
    msg:"ET WEB_SPECIFIC_APPS Apache OFBiz Pre-Auth Remote Code Execution Attempt (CVE-2024-38856)";
    flow:established,to_server;
    http.method;
    content:"POST";
    http.uri;
    content:"/webtools/control/";
    fast_pattern;
    startswith;
    pcre:"/^(?:TestService|view|showDateTime|main|forgotPassword)/R";
    content:"ProgramExport";
    endswith;
    http.request_body;
    content:"groovyProgram";
    startswith;
    reference:url,blog.sonicwall.com/en-us/2024/08/sonicwall-discovers-second-critical-apache-ofbiz-zero-day-vulnerability/;
    reference:cve,2024-38856;
    classtype:attempted-admin;
    sid:2054947;
    rev:1;
    metadata:affected_product Apache_OFBiz, attack_target Server, tls_state TLSDecrypt, created_at 2024_08_06, cve CVE_2024_38856, deployment Perimeter, deployment Internal, deployment SSLDecrypt, performance_impact Low, confidence High, signature_severity Major, updated_at 2024_08_06;
    target:dest_ip;
)

 



## URL 인코딩 문자열


%0a는 URL 인코딩된 문자열로, 
이 문자열은 ASCII 코드에서 줄 바꿈(newline)을 의미하는 \n 문자에 해당합니다.

URL 인코딩에서는 특정 특수 문자를 인코딩하여 안전하게 전송하기 위해 16진수 값 앞에 %를 붙입니다. 예를 들어, ASCII 코드에서 줄 바꿈은 16진수 0A로 표현되며, 이를 URL로 인코딩하면 %0a가 됩니다.

따라서, %0a는 줄 바꿈(newline) 문자를 의미하며, URL 인코딩된 데이터를 해석할 때 이를 줄 바꿈으로 변환해 명령어를 실행하게 됩니다.