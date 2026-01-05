# reverse-proxy

A reverse proxy is a server that sits in front of one or more web servers, intercepting requests from clients.

With a reverse proxy, when clients send requests to the origin server of a website, those requests are intercepted at the network edge (where the device, or the local network containing the device, communicates with the Internet) by the reverse proxy server. The reverse proxy server will then send requests to and receive responses from the origin server. Ensures that no client ever communicates directly with that origin server.

Reverse proxies are typically implemented to help increase security, performance, and reliability. 

![](https://github.com/mrbrogrammer/reverse-proxy/blob/main/fig01.png)

Below I outline some of the benefits of a reverse proxy:

* Load balancing - control traffic
* Protection from attacks
* Global server load balancing (GSLB) - control traffic with geographical constrains
* Caching
* SSL encryption
