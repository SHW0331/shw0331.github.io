alert http any any -> any any (
    msg:"CUPS Reflected DDoS IPP Request";
    content:"POST";
    http_method;
    content:"/printers/";
    http_uri;
    content:"Content-Type: application/ipp";
    http_header;
    content:"User-Agent: CUPS/";
    http_header;
    content:"printer-uri";
    http_client_body;
    metadata:service http;
    reference:cve,2024-47076,2024-47175,2024-47177;
    sid:100004;
    rev:1;
)​ 

alert http any any -> any any (msg:"CUPS Reflected DDoS IPP Request"; 
    flow:to_server,established;
    content:"/printers"; http_uri; 
    content:"POST"; http_method; 
    content:"application/ipp"; http_header; 
    content:"CUPS/"; http_header; 
    content:"printer-uri"; http_client_body; 
    threshold:type limit, track by_src, count 1, seconds 10;
    metadata:service http; 
    reference:url,https://akamai.com/blog/security-research/2024/october-cups-ddos-threat;
    sid:100004; 
   rev:2;)

   CVE-2024-47176 in cups-browsed, which coerces a request to an attacker-controlled address

	
alert http any any -> any any (msg:"CUPS Reflected DDoS IPP Request"; content:"POST";http_method;content:"/printers/";http_uri;content:"Content-Type: application/ipp"; http_header; content:"User-Agent: CUPS/"; http_header; content:"printer-uri"; http_client_body; metadata:service http; reference:cve,2024-47076,2024-47175,2024-47177;sid:100004;priority:1;rev:1;)​ 

 