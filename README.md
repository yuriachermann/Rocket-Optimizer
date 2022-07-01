# Prerequisites
* [OpeRocket 15.03](https://github.com/openrocket/openrocket/releases/download/release-15.03/OpenRocket-15.03.jar)
* Python >= 3.6
* Java JDK 1.8
  + [Oracle Java SE Development Kit 8](https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html)
  + OpenJDK for Ubuntu: `sudo apt-get install openjdk-8-jre`

# Setup JDK
### Linux
For most people jpype will be able to automatically find the JDK. However, if it fails or you want to be sure you are using the correct version, add the JDK path to a JAVA_HOME environment variable:

* Find installation directory (`e.g. /usr/lib/jvm/[YOUR JDK 1.8 FOLDER HERE]`)
* Open the `~/.bashrc` file with your favorite text editor (will likely need sudo privileges)
* Add the following line to the `~/.bashrc` file:
```
export JAVA_HOME="/usr/lib/jvm/[YOUR JDK 1.8 FOLDER HERE]"
```
* Restart your terminal or run the following for the changes to take effect:
```
source ~/.bashrc
```

### Windows
* Set Windows environment variables to the following:
   + Oracle
    ```
    JAVA_HOME = C:\Program Files\Java\[YOUR JDK 1.8 FOLDER HERE]
    ```
   + OpenJDK
    ```
    JAVA_HOME = C:\Program Files\ojdkbuild\[YOUR JDK 1.8 FOLDER HERE]
    ```
    
# Setup OpenRocket
* Download the [OpenRocket-15.03.jar](https://github.com/openrocket/openrocket/releases/download/release-15.03/OpenRocket-15.03.jar) file
* Right-click the file and select ```Properties```
* On the the ```Permissions``` tab, enable the ```Allow executing file as program``` option 


# Installing orhelper

Make sure to have https://pypi.python.org/simple as a repository channel on your environment

* Install orhelper from pip
```
pip install orhelper
```

* Set environment variable CLASSPATH path to OpenRocket .jar file. (Only required if it's not already at .\OpenRocket-15.03.jar)
```
CLASSPATH=\some\path\to\OpenRocket-15.03.jar
```

# Adding the motor to OpenRocket
* Open the [motor file link](https://raw.githubusercontent.com/yuriachermann/tcc-openrocket/main/Acrux.eng?token=AJPQFUF7QGM6Z4NF5BFP2TLBJSUTG) and save as "Acrux.eng"
* Execute OpenRocket
* Select the ```Edit``` tab and click on ```Preferences```
* On ```User-defined thrust curves``` click on ```Add``` and select the path to the ```Acrux.eng``` file

# PSO running
![gif_model](https://media3.giphy.com/media/MlDLrTnHwdQK3oJmhV/giphy.gif?cid=790b7611b905a11a0cd569c886d3c65595fdc852f09e906f&rid=giphy.gif&ct=g)
![gif](https://media3.giphy.com/media/b2eW0Q6xJXvIcaxVPU/giphy.gif?cid=790b7611318fb0323861126144d8f8378778bd2691c03af6&rid=giphy.gif&ct=g)

# Credits
* Sampo Niskanen for the original simulator development: [Documentation](https://github.com/openrocket/openrocket/releases/download/OpenRocket_technical_documentation-v13.05/OpenRocket_technical_documentation-v13.05.pdf)
* @SilentSys for the advising and consolidation of orhelper: [Source](https://github.com/SilentSys/orhelper)
* And of course everyone who has contributed to OpenRocket over the years.
