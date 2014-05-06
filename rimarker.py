marker_black = (0.20, 0.20, 0.20)
marker_white = (0.98, 0.98, 0.98)

def draw_marker(ri, pattern, position, size, border_width):
    x0, y0 = position
    w, h = size
    w_b = border_width
    w_c = w / (pattern.shape[0] + 1)
    h_c = h / (pattern.shape[1] + 1)
    ri.Color(marker_white)
    draw_border(ri,
                (x0 - w_b, y0 - w_b),
                (w + w_b*2, h + w_b*2),
                (w_b, w_b))    
    ri.Color(marker_black)
    draw_border(ri, position, size, (w_c, h_c))
    draw_pattern(ri, pattern,
                 (x0 + w_c, y0 + h_c),
                 (w - w_c*2, h - h_c*2))

def draw_border(ri, position, size, border_size):
    x0, y0 = position
    w, h = size
    w_b, h_b = border_size
    def rect(x, y, w, h):        
        ri.Polygon(P=[x, y, 0,
                      x + w, y, 0,
                      x + w, y + h, 0,
                      x, y + h, 0])
    # Left
    rect(x0, y0, w_b, h)
    # Right
    rect(x0 + w - w_b, y0, w_b, h)
    # Bottom
    rect(x0 + w_b, y0, w - w_b, h_b)
    # Top
    rect(x0 + w_b, y0 + h - h_b, w - w_b, h_b)
    

def draw_pattern(ri, pattern, position, size):
    x0, y0 = position
    w, h = size
    w_b, h_b = w / pattern.shape[0], h / pattern.shape[1]
    
    def block(white, x, y):
        ri.Color(marker_white if white else marker_black)
        ri.Polygon(P=[x, y, 0,
                      x + w_b, y, 0,
                      x + w_b, y + h_b, 0,
                      x, y + h_b, 0])                      
    
    for i in range(pattern.shape[1]):
        for j in range(pattern.shape[0]):
            block(pattern[j, i],
                  x0 + j * w_b,
                  y0 + h - (i + 1) * h_b)


if __name__ == "__main__":
    import cgkit.cri
    import simple
    
    ri = cgkit.cri.loadRI("ri")
    cgkit.cri.importRINames(ri, globals())
    
    RiBegin(RI_NULL)
    RiFormat(1024, 768, 1)
    RiDisplay("simple_0.tif", RI_FILE, "rgb")
    RiPixelSamples(3, 3)
    RiProjection("perspective", "fov", 45)
    RiTranslate(0, 0, 2)
    RiWorldBegin()
    RiLightSource("pointlight", "from", (3, 0, -3), intensity=20)
    RiSurface("matte")
    draw_marker(ri, simple.SimplePattern(0), (-0.5, -0.5), (1.0, 1.0), 0.1)
    RiWorldEnd()
    RiEnd()

