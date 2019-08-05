import pyspeckit
from spectral_cube import SpectralCube
from astropy import units as u
import pylab as pl

cube11 = SpectralCube.read(filename='unpb_mosaic_11_trim.fits', allow_huge_operations=True)
cube11.allow_huge_operations=True
cube11 = cube11.to(u.K)
cube11 = cube11.with_spectral_unit(u.km/u.s, velocity_convention='radio')

n11cube = pyspeckit.Cube(cube = cube11)

cube22 = SpectralCube.read('unpb_mosaic_22_trim.fits', allow_huge_operations=True)
cube22.allow_huge_operations=True
cube22 = cube22.to(u.K)
cube22 = cube22.with_spectral_unit(u.km/u.s, velocity_convention='radio')

n22cube = pyspeckit.Cube(cube = cube22)

cube44 = SpectralCube.read('unpb_mosaic_44_trim.fits', allow_huge_operations=True)
cube44.allow_huge_operations=True
cube44 = cube44.to(u.K)
cube44 = cube44.with_spectral_unit(u.km/u.s, velocity_convention='radio')

n44cube = pyspeckit.Cube(cube = cube44)

cube55 = SpectralCube.read('unpb_mosaic_55_trim.fits', allow_huge_operations=True)
cube55.allow_huge_operations=True
cube55 = cube55.to(u.K)
cube55 = cube55.with_spectral_unit(u.km/u.s, velocity_convention='radio')

n55cube = pyspeckit.Cube(cube = cube55)

#Extracting Spectrum

x = 143
y = 160

sp11 = n11cube.get_spectrum(x,y) 
sp22 = n22cube.get_spectrum(x,y) 
sp44 = n44cube.get_spectrum(x,y)
sp55 = n55cube.get_spectrum(x,y)

#sp11.plotter()
#sp22.plotter()
#sp33.plotter() #Plots spectrum

sp11.xarr.refX = pyspeckit.spectrum.models.ammonia.freq_dict['oneone']
sp22.xarr.refX = pyspeckit.spectrum.models.ammonia.freq_dict['twotwo']
sp44.xarr.refX = pyspeckit.spectrum.models.ammonia.freq_dict['fourfour']
sp55.xarr.refX = pyspeckit.spectrum.models.ammonia.freq_dict['fivefive']

sp11.xarr.velocity_convention='radio'
sp22.xarr.velocity_convention='radio'
sp44.xarr.velocity_convention='radio'
sp55.xarr.velocity_convention='radio'

input_dict = {'oneone':sp11, 'twotwo':sp22, 'fourfour':sp44, 'fivefive':sp55}

spf = pyspeckit.wrappers.fitnh3.fitnh3tkin(input_dict, dobaseline=False)



pl.show()
