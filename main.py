import pygame as pg

SIZE = (800, 600)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pg.init()

window = pg.display.set_mode(SIZE)

large_font = pg.font.Font('liberationserif.ttf', 32) 
small_font = pg.font.Font('liberationserif.ttf', 20) 

width = window.get_width()
height = window.get_height()

gen_text = large_font.render('Generate Structure', True, BLACK)
export_svg_text = small_font.render('Export as SVG', True, BLACK)
export_png_text = small_font.render('Export as PNG', True, BLACK)

gen_text_rect = gen_text.get_rect(center = (width / 2, height - 48))
export_svg_text_rect = export_svg_text.get_rect(center = (width - 80, 24))
export_png_text_rect = export_png_text.get_rect(center = (width - 80, 48))

running = True

while running:
    window.fill(WHITE)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    window.blit(gen_text, gen_text_rect)
    window.blit(export_svg_text, export_svg_text_rect)
    window.blit(export_png_text, export_png_text_rect)

    pg.display.update()

pg.quit()
