# credits to @lomnom
py
num_grid=lambda l: [['#' if i=='#' else str(sum([len(l)>(y+Y)>=0 and len(l)>(x+X)>=0 and l[(y+Y)][(x+X)]=='#'for X,Y in((0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1))]))for x,i in enumerate(r)]for y,r in enumerate(l)]
