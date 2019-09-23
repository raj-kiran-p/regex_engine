<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/raj-kiran-p/regex_engine">
    <img src="https://static.wixstatic.com/media/03a041_a8d70333218e4f2691fb6a30d7219923~mv2.png/v1/fill/w_200,h_200/regex-engine.png" alt="Logo" width="160" height="160">
  </a>
  <h3 align="center">Regex Engine</h3>
  <p align="center">
    An awesome package to generate regex
    <a href="https://github.com/raj-kiran-p/regex_engine/issues">Report Bug</a>
    ·
    <a href="https://github.com/raj-kiran-p/regex_engine/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Coded With Language](#coded-with-language)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

Generating regex can sometimes be complicated. That is why we are introducing this package to help you get things done.

Supported functionalities : 
- Regex Generation for Numerical Range

### What does each functionalities do?

__1. Regex Generation for Numerical Range__   

Generate regex given a numerical range, So when given a new number between this range the regex will match.

_Person who has motivated me to start this repository is listed in the acknowledgments._

### Coded With Language
* [Python 3.6](https://python.org)



<!-- GETTING STARTED -->
## Getting Started

Simply install the package, import it in your python code and run the method needed.
Look at the docstring or source code to understand what is happening. 

### Prerequisites

Python 3.6 or greater


### Installation

```sh
pip install regex-engine
```


<!-- USAGE EXAMPLES -->
## Usage

### 1. Regex Generation for Numerical Range

__You get what you give :__ If given numbers are integers you get a regex that will only match with integer and if floating-point numbers are given it only match with floating-point number.

Supports integer and floating-point numbers. It can even be a negative range.

```python
from regex_engine import generator
generate = generator()
regex1 = generate.numerical_range(5,89)
regex2 = generate.numerical_range(81.78,250.23)
regex3 = generate.numerical_range(-65,12)
```
Example regex generated for 25-53
```
^([3-4][0-9]|2[5-9]|5[0-3])$
```

The regex might not be optimal but it will surely serve the purpose.

The problem of checking a number is within a range might have been simple if you didn't choose the regex path.   
`if a <= your_input_number <=b` would have simply solved the same problem.

We dedicate this method in the package to the people who are pursuing a different path or thinking out of the box.



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/raj-kiran-p/regex_engine/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Raj Kiran P - [@raj_kiran_p](http://www.twitter.com/raj_kiran_p) - rajkiranjp@gmail.com   
GitHub : [https://github.com/raj-kiran-p](https://github.com/raj-kiran-p)   
Website : [https://rajkiranp.com](https://rajkiranp.com)


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Ashwin Rajeev](https://github.com/ashwin-rajeev)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/raj-kiran-p/regex_engine?style=flat-square
[contributors-url]: https://github.com/raj-kiran-p/regex_engine/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/raj-kiran-p/regex_engine?style=flat-square
[forks-url]: https://github.com/raj-kiran-p/regex_engine/network/members
[stars-shield]: https://img.shields.io/github/stars/raj-kiran-p/regex_engine?style=flat-square
[stars-url]: https://github.com/raj-kiran-p/regex_engine/stargazers
[issues-shield]: https://img.shields.io/github/issues/raj-kiran-p/regex_engine?style=flat-square
[issues-url]: https://github.com/raj-kiran-p/regex_engine/issues
[license-shield]: https://img.shields.io/github/license/raj-kiran-p/regex_engine?style=flat-square
[license-url]: https://github.com/raj-kiran-p/regex_engine/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/rajkiranjp
