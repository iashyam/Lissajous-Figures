
# Lissajous Figures

Making Lissajous's Figures is a teadous process when we start from tracing the sine curves and making the superposition. It was very difficuilt for me too. Then I realised I had programming power. So I made this program.

## What are Lissajous's Figures?

When two perpendicular simpoer harmonic motions superimpose, they make some beautiful images and it is called Lissajous's Figures. 

Genral equation for Lissajous's Figures is given by 

$$\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{2xy}{ab}\cos\delta=\sin^2\delta$$


[Read More](https://en.wikipedia.org/wiki/Lissajous_curve)

## How to draw them?

In this program I have plotted the first SHM on x axis and the other SHM on y axis. 
$$x=a\sin(t\omega_1)$$
$$y=b\sin(t\omega_2+\delta)$$

I have gievn sliders to control

1. the phase differace delta
2. The ratio of frequencies w1/w2
3. The Ratio of amplitudes


## Demo

![demo](https://github.com/iashyam/Lissajous-Figures/blob/main/gif.gif)


## Installation

### Requarmetnes 

 Python: [Download from here](https://www.python.org/ftp/python/3.10.1/python-3.10.1-amd64.exe) and Install


 git: [get from here](https://git-scm.com/download/win)


Install my-project with command line

Install numpy and matplotlib
```cmd
pip install numpy
pip install matplotlib
```

Clone the Project
```cmd
  git clone https://github.com/iashyam/Lissajous-Figures
```
To to the folder
```cmd
  cd Lissajous Figures
```
Open it with Python

```cmd
python lissajous.py
```
    
## Contributing

Contributions are always welcome!


Please adhere to this project's `code of conduct`.


## License

[MIT](https://github.com/iashyam/Lissajous-Figures/blob/main/LICENSE)

Copyright Shyam Sunder &copy; 2021
