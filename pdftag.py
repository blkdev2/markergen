import simple

def draw_marker(pdf, pattern, position, size, border_width):
    w, h = size
    w_b = border_width
    w_c = w / (pattern.shape[0] + 1)
    h_c = h / (pattern.shape[1] + 1)
    pdf.set_draw_color(192, 192, 192)
    pdf.rect(position[0] - w_b,
             position[1] - w_b,
             size[0] + 2 * w_b,
             size[1] + 2 * w_b,
             'D')
    pdf.set_draw_color(0, 0, 0)
    pdf.set_fill_color(0, 0, 0)
    pdf.rect(position[0],
             position[1],
             size[0],
             size[1],
             'FD')
    draw_pattern(pdf,
                 pattern,
                 [p + w_c for p in position],
                 [s - w_c * 2 for s in size])
                 

def draw_pattern(pdf, pattern, position, size):
    x0, y0 = position
    w, h = size
    w_c, h_c = [s / n for s, n in zip(size, pattern.shape)]
    
    def set_bw(black):
        color = (0, 0, 0) if black else (255, 255, 255)
        pdf.set_fill_color(*color)
        pdf.set_draw_color(*color)

    for i in range(pattern.shape[1]):
        for j in range(pattern.shape[0]):
            set_bw(not pattern[j, i])
            pdf.rect(x0 + j * w_c,
                     y0 + i * h_c,
                     w_c,
                     h_c,
                     'DF')
