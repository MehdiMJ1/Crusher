<h1 align='center'>
 Crusher
</h1>

<p align='center'>
A Powerful DDoS/DoS Tool
</p>

[![GitHub license](https://img.shields.io/github/license/Paxv28/Crusher?style=flat-square)](https://github.com/Paxv28/Crusher/blob/master/LICENSE)
[![GitHub forks](https://img.shields.io/github/forks/Paxv28/Crusher?style=flat-square)](https://github.com/Paxv28/Crusher/network)
[![GitHub stars](https://img.shields.io/github/stars/Paxv28/Crusher?style=flat-square)](https://github.com/Paxv28/Crusher/stargazers) 
[![GitHub issues](https://img.shields.io/github/issues/Paxv28/Crusher?style=flat-square)](https://github.com/Paxv28/Crusher/issues)
* [Setup](#Setup)
* [Usage](#Usage)
* [Releases](#Releases)
* [Contributing](#Contributing)
* [License](#License)

**What is a DoS Attack?**

In computing, a denial-of-service attack (DoS attack)
is a cyber-attack in which the perpetrator seeks to make a 
machine or network resource unavailable to its intended users 
by temporarily or indefinitely disrupting services of a host 
connected to the Internet. 
Denial of service is typically accomplished by flooding the targeted 
machine or resource with superfluous requests in an attempt to 
overload systems and prevent some or all legitimate requests from being fulfilled.


## Setup

**Linux**
```sh
$ sudo apt-get install python3
```
**OSX**
```sh
$ brew install python
```


## Usage

```sh
python3 Crusher.py <IP> <PORT> <MODE>
```

* `python3 Crusher.py 10.0.0.1 80 udp`
* `python3 Crusher.py 10.0.0.1 80 tcp`
* `python3 Crusher.py 10.0.0.1 80 http`
> Use Ctrl + Z to avoid long error messages

## Releases
* `v1.1`
  * Added HTTP Mode

* `v1.0`
  * Work in Progress


## Contributing
* fork the project
* Create a Branch 
* add your modifications


## License
Crusher is released under the [BSD-3-Clause](https://github.com/Paxv28/Crusher/blob/master/LICENSE)
