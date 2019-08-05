lm.defineoutputimage(nx=1000, outputimage='test_mosaic.linmos', imagecenter='19h23m43.512 14d30m39.998' )
lm.makemosaic(images=['IRS2_11_cleaned_03.image', 'W51_NH3_11_02.image'], weightimages=['IRS2_11_cleaned_03.pb', 'W51_NH3_11_02.pb'])
#lm.makemosaic(images='submosaic.image', weightimages='submosaic.flux', imageweighttype=0, weighttype=1)
#lm.setoutputimage(outputimage='test_mosaic.linmos', outputweight='test_mosaic.weight', imageweighttype=0, weighttype=2)
