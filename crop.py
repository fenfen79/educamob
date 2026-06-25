import sys
try:
    from PIL import Image, ImageChops
    
    def trim(im):
        # Converte para RGBA se não for
        im = im.convert("RGBA")
        # Pega a cor do pixel 0,0 (fundo branco)
        bg = Image.new(im.mode, im.size, (255, 255, 255, 255))
        diff = ImageChops.difference(im, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        if bbox:
            return im.crop(bbox)
        return im

    im = Image.open('shared/assets/BASE-V1.png')
    im = trim(im)
    im.save('shared/assets/BASE-V1-cropped.png')
    print("Cropped successfully")
except ImportError:
    print("PIL not installed")
except Exception as e:
    print(f"Error: {e}")
