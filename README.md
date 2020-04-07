# 109titration_2019
Math Project : 109

__109titration__

Project Maths

__Members__ : Martin Le morvan
          Esteffe Liam
          
 ![helper](https://cdn.discordapp.com/attachments/694987281173315685/697027421660250162/usage.png)
          
 ![image1](https://cdn.discordapp.com/attachments/694987281173315685/697027393566801981/109.png)
          
To find the concentration of preservative in the soda, the volume of added titrant at the equivalence point
(ie at the middle of the pH-jump) must be read. There are two main approaches to do so:

• __the derivative method__, which consists in calculating the derivative of the curve; the equivalence point
matches with the maximum of this derivative,
• __the parallel tangents method__, which consists in drawing two parallel tangents from one part and an-
other of the pH-jump, then to draw a third straight line equidistant from the two first. The equivalence
point is at the intersection between this last line and the curve.


You must code the first approach here. Your program has to read titrant volume (in ml) and pH couples from
a csv file, and output:
__1__.  the derivative values for each given volume,
__2__. the closest point from the equivalence point amongst those given points,
__3__. the second derivative values for each given volume,
__4__. an estimate of the second derivative values every 0.1 ml around the above closest point from the
   equivalence point, using linear interpolation,
__5__. the proper equivalence point, estimated from the second derivative

![image3](https://cdn.discordapp.com/attachments/694987281173315685/697027391461261392/3.png)
