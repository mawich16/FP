# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle

def main():
    screen = turtle.Screen()
    t = turtle.Turtle()

    # Use t.up(), t.down() and t.goto(x, y)

    # Put your code here
    file=open('drawing.txt','r')
    
    for i in file:
        i=i.strip()
        if 'UP'==i:
            t.up()
        elif 'DOWN'==i:
            t.down()
        else:
           l=i.split()
           t.goto(float(l[0]),float(l[1]))

    file.close()



    # Wait until window is closed
    screen.mainloop()


if __name__ == "__main__":
    main()

