tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(myData):
    
    colWidth = [0] * len(myData)
    
    for width in range(len(myData)):
        maxWidth = 0
        
        for lonS in range(1,len(myData[width])):
            if len(myData[width][lonS]) > len(myData[width][maxWidth]):
                maxWidth = lonS
            
        colWidth[width] = len(myData[width][maxWidth])
       
    for x in range(len(myData[0])):
        toPrint = []
        
        for y in range(len(myData)):
            
            toPrint.append(myData[y][x].rjust(colWidth[y]))

        print(' '.join(toPrint))

printTable(tableData)



