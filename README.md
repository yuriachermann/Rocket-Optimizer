<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://website.com">
    <img src="https://i.imgur.com/OTxhqE6.png" alt="Logo" width="128" height="128">
  </a>

<h3 align="center">Rocket Optimizer</h3>

  <p align="center">
    A Python project for optimizing your rocket projects using OpenRocket and PSO
    <br />
    <a href="https://github.com/yuriachermann/Rocket-Optimization"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://website.com">View Demo</a>
    ·
    <a href="https://github.com/yuriachermann/Rocket-Optimization/issues">Report Bug</a>
    ·
    <a href="https://github.com/yuriachermann/Rocket-Optimization/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

Rocket Optimizer is a Python script that uses OpenRocket to optimize rocket designs. It uses a genetic algorithm to find the best rocket design for a given set of constraints. The script is designed to be used with the [OpenRocket](https://openrocket.info/) rocket design software.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

* [![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* [OpeRocket 15.03](https://github.com/openrocket/openrocket/releases/download/release-15.03/OpenRocket-15.03.jar)
* Python >= 3.6
* Java JDK 1.8
  + [Oracle Java SE Development Kit 8](https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html)
  + OpenJDK for Ubuntu: `sudo apt-get install openjdk-8-jre`


### Installation

#### Linux
For most people jpype will be able to automatically find the JDK. However, if it fails or you want to be sure you are using the correct version, add the JDK path to a JAVA_HOME environment variable:

* Find installation directory (`e.g. /usr/lib/jvm/[YOUR JDK 1.8 FOLDER HERE]`)
* Open the `~/.bashrc` file with your favorite text editor (will likely need sudo privileges)
* Add the following line to the `~/.bashrc` file:
```console
export JAVA_HOME="/usr/lib/jvm/[YOUR JDK 1.8 FOLDER HERE]"
```
* Restart your terminal or run the following for the changes to take effect:
```console
source ~/.bashrc
```

#### Windows
* Set Windows environment variables to the following:
  + If Oracle
    ```console
    JAVA_HOME = C:\Program Files\Java\[YOUR JDK 1.8 FOLDER HERE]
    ```
  + If OpenJDK
    ```console
    JAVA_HOME = C:\Program Files\ojdkbuild\[YOUR JDK 1.8 FOLDER HERE]
    ```

#### Setup OpenRocket
* Download the [OpenRocket-15.03.jar](https://github.com/openrocket/openrocket/releases/download/release-15.03/OpenRocket-15.03.jar) file
* Right-click the file and select ```Properties```
* On the ```Permissions``` tab, enable the ```Allow executing file as program``` option


#### Installing orhelper

Make sure to have https://pypi.python.org/simple as a repository channel on your environment

* Install orhelper from pip
```
pip install orhelper
```

* Set environment variable CLASSPATH path to OpenRocket .jar file. (Only required if it's not already at .\OpenRocket-15.03.jar)
```
CLASSPATH=\some\path\to\OpenRocket-15.03.jar
```

#### Adding the motor to OpenRocket
* Open the [motor file link](https://raw.githubusercontent.com/yuriachermann/tcc-openrocket/main/Acrux.eng?token=AJPQFUF7QGM6Z4NF5BFP2TLBJSUTG) and save as "Acrux.eng"
* Execute OpenRocket
* Select the ```Edit``` tab and click on ```Preferences```
* On ```User-defined thrust curves``` click on ```Add``` and select the path to the ```Acrux.eng``` file
* Click ```OK``` to save the changes

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

### PSO running
![gif_model](https://media3.giphy.com/media/MlDLrTnHwdQK3oJmhV/giphy.gif?cid=790b7611b905a11a0cd569c886d3c65595fdc852f09e906f&rid=giphy.gif&ct=g)
![gif](https://media3.giphy.com/media/b2eW0Q6xJXvIcaxVPU/giphy.gif?cid=790b7611318fb0323861126144d8f8378778bd2691c03af6&rid=giphy.gif&ct=g)


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Yuri Winche Achermann - [@YuriAchermann](https://twitter.com/YuriAchermann) - yuri.achermann@gmail.com


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Sampo Niskanen for the original simulator development: [Documentation](https://github.com/openrocket/openrocket/releases/download/OpenRocket_technical_documentation-v13.05/OpenRocket_technical_documentation-v13.05.pdf)
* @SilentSys for the advising and consolidation of orhelper: [Source](https://github.com/SilentSys/orhelper)
* And of course everyone who has contributed to OpenRocket over the years.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: images/screenshot.png
[Python]: https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python
[Python-url]: https://www.python.org
