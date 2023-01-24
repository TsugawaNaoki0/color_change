import sys

selected_color = str(sys.argv[1])

if (selected_color == "black"):
    selected_css = ".main{background:black;}.graph1,.graph2{text-align:center;}.circle1,.circle2{width:35%;margin-left:5%;margin-right:5%;margin-top:5%;margin-bottom:5%;}"
elif (selected_color == "blue"):
    selected_css = ".main{background:blue;}.graph1,.graph2{text-align:center;}.circle1,.circle2{width:35%;margin-left:5%;margin-right:5%;margin-top:5%;margin-bottom:5%;}"
elif (selected_color == "red"):
    selected_css = ".main{background:red;}.graph1,.graph2{text-align:center;}.circle1,.circle2{width:35%;margin-left:5%;margin-right:5%;margin-top:5%;margin-bottom:5%;}"
elif (selected_color == "green"):
    selected_css = ".main{background:green;}.graph1,.graph2{text-align:center;}.circle1,.circle2{width:35%;margin-left:5%;margin-right:5%;margin-top:5%;margin-bottom:5%;}"
elif (selected_color == "purple"):
    selected_css = ".main{background:purple;}.graph1,.graph2{text-align:center;}.circle1,.circle2{width:35%;margin-left:5%;margin-right:5%;margin-top:5%;margin-bottom:5%;}"
elif (selected_color == "yellow"):
    selected_css = ".main{background:yellow;}.graph1,.graph2{text-align:center;}.circle1,.circle2{width:35%;margin-left:5%;margin-right:5%;margin-top:5%;margin-bottom:5%;}"

# print(selected_css)

path = './home.css'


f = open(path, 'r', encoding='UTF-8')
now_css = f.read()


f = open(path, 'w')
f.write(selected_css)

f.close()
