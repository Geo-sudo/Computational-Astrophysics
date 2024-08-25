# Binary Star System Simualtion

This is a realistic astrophysical simulation of a **Binary Star System**, written in `Python` using the `matplotlib` library.

### Table of Contents

- [Background On Binary Stars](#background-on-binary-stars)
- [How To Run](#how-to-run)
- [The Physics](#the-physics)


# Background On Binary Stars

Did you know that **Sirius** the brightes "star" in the nightsky isn't a star! It's a Binary Star System: two stars that are graviationally bound together ([Read More](https://en.wikipedia.org/wiki/Binary_star)). <br>
We see it as one source of light because of the massive distance between us and the star; when you look at your LED light bulb you don't see each LED, but you see their light as one.

<figure style="text-align: center;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/This_artist’s_impression_shows_the_strange_object_AR_Scorpii.jpg/800px-This_artist’s_impression_shows_the_strange_object_AR_Scorpii.jpg" alt="Artist's impression of the binary star system AR Scorpii" style="display: block; margin: 0 auto;">
  <figcaption>Figure 1: Artist's impression of the binary star system AR Scorpii. By M. Garlick/University of Warwick/ESO - <a href="http://www.eso.org/public/images/eso1627a/">ESO</a>, CC BY 4.0.</figcaption>
</figure>

<br>

The way to detect these is by using precise equipment that can detect the faintest of brightness changes over time (see the image below) caused by eclipses. If the lumnisoity of the star changes *periodically*, then it's a star system. Further carefull analysis of the lumnisotiy over time graph will tell us if it's a Binary Star System or if it's a bigger party of "fireballs."

<figure>
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/0d/Light_curve_of_binary_star_Kepler-16.jpg" alt="Light curve of binary star Kepler-16">
  <figcaption style="text-align: center;">Figure 2: Light curve of binary star Kepler-16. By NASA.</figcaption>
</figure>

# How To Run

**Run it like any Python file using:** <br>
`python Run_Binary_System.py`

The simulation has two modes: *viewing* and *saving*. `save=False` allows you to view the animation in a window, while `save=True` will, in addition to viewing the animation, save it in webm format in the current directory.

<br>

**Running the simulation will use these default values:** <br>
- `t=1e9` ---> Duration to run the animation in viewing mode in days.
- `save=False` ---> Defines whether you're using *viewing* or *saving* mode.
- `Sirius=False` ---> By default the used data is a random stable orbit. Setting this to True will use real-world data from the Sirius binary system.
- `size=50` ---> This defines the cubic size of the simulation world in AU.
- `dt=200` ---> The timestep taken for each calculation in days.

<br>

> Note: You can run the Sirius system example or the given stable one from the terminal. Using other data will require you to hard code it in the [Run_Binary_System.py](Run_Binary_System.py) as it will be cumbersome to pass that many arguments. <br>This also applies to the configuration of the animation in *saving* mode.

# The Physics

> The used units are AU, M0, and days for L, M, and T, respectively.
