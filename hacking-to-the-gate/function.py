def getBestColours(parent, number):
    ratio = []
    if(len(parent) < number):
        number = len(parent)

    for i in range(0, len(parent)):
        ratio.append(parent[i]['ratio'])

    ratio.sort(reverse=True)

    ratio = ratio[:number]

    resultColor = []

     # COMPARE WITH ORIGINAL JSON
    for i in range(0, len(ratio)):
         for j in range(0, len(parent)):
              if(ratio[i] == parent[j]['ratio']):
                    resultColor.append(parent[j]['colorGeneralCategory'])
                    # print(resultColor)

    return resultColor

def getBestStyles(parent, number):
    confidence = []
    if(len(parent) < number):
        number = len(parent)

    for i in range(0, len(parent)):
        confidence.append(parent[i]['confidence'])

    confidence.sort(reverse=True)

    confidence = confidence[:number]
    
    resultStyles = []

     # COMPARE WITH ORIGINAL JSON
    for i in range(0, len(confidence)):
         for j in range(0, len(parent)):
              if(confidence[i] == parent[j]['confidence']):
                   resultStyles.append(parent[j]['styleName'])

    return resultStyles

def getBestGarments(parent, number): 
    if(len(parent) < number):
        numbers = len(parent)
 
    confidence = []

    for i in range(0, len(parent)):
        confidence.append(parent[i]['confidence'])
        
    confidence.sort(reverse=True)

    confidence = confidence[:number]


    resultGarment = []

     # COMPARE WITH ORIGINAL JSON
    for i in range(0, len(confidence)):
         for j in range(0, len(parent)):
              if(confidence[i] == parent[j]['confidence']):
                   resultGarment.append(parent[j]['typeName'])

    return resultGarment

def prepareData(colors, styles, garments):
     data_insert = []
     for i in range (0,3):
          try:
               data_insert.append(colors[i])
          except IndexError:
               data_insert.append('')
     for i in range (0,3):
          try:
               data_insert.append(styles[i])
          except IndexError:
               data_insert.append('')
     for i in range (0,1):
          try:
               data_insert.append(garments[i])
          except IndexError:
               data_insert.append('')
     
     return data_insert
