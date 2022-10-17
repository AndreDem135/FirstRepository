for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:  
            for v in 0, 1:
                if (not (y<=x) or (z<=v) or not (z)) == 0:
                    print(y, x, z, v)
            
    