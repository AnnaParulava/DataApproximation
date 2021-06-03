% rebase('layout.tpl', title=title, year=year, answer=answer)

<style>
   .button {
  background-color: #242425;
  border: none;
  color: white;
  padding: 5px 25px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  border-radius: 16px;
}
}
</style>
<div class="jumbotron" style="background-color: #aaf0d1; border-radius: 0 0 15px 15px;">
    <h1 style="font-size: 35px; margin-bottom: 40px;">Statement of the task:</h1>
    <p style="font-size: 16px;" class="lead">Using the least squares method, the function y = f (x), given in the table, is approximated by a polynomial of
    the second degree y = P2 (x) = a0 + a1x + a2x2. Get the coefficients of the quadratic regression line a0, a1 and a2, the coefficient of determinism R2.
</p>
    <p><a href="https://en.wikipedia.org/wiki/Least_squares" class="button">Learn more about least squares method</a></p>
</div>
<h1 style="margin: 40px 0; padding-top: 40px; text-align: center;">Function aproskimation</h1>
<p style="font-size: 16px; margin-bottom: 20px;">On this page, you can approximate function and get obtaining coefficients of linear regression and coefficient of determinism </p>
<div class="junbotron">

	
	<div style="background-color: #aaf0d1; border-radius: 15px; padding: 20px;"><p style="font-size: 14px;">Specify the amount of source data: </p>
    <form method='post'>
    %try:
		<p><input type="Number"  name="num" value={{rows}} placeholder="" min=1 max=99 ></input></p> 
        %except NameError:
        <p><input type="Number"  name="num" placeholder="" min=1 max=99 style="border-radius: 5px;"></input></p> 
        %finally:
        <p> <input name="subm" type="submit"  class="button button" value="Ok"></p>
    </form>
    
    %try:
    <form method='post' style="margin: 60px 0;">
    <p><input type="Number"  name="num" value={{rows}} placeholder="Number of graph vertices" min=1 max=99 hidden></input></p> 
        % include('make_table.tpl', title='make_table', rows=rows)
    <p> <input name="subm" type="submit"  class="button button" value="Calculate"></p>
        
    </form>
        %except NameError:
    %pass
    %finally:
    <h2 class="answer">{{answer}}</h2>
    </div>

    <h2 style="margin: 90px 0 30px 0;">Linear regression</h2>
    <div style="display: grid; grid-template-columns: 1fr 3fr;"><div><img style="" src="static\res\lin.png" width="300" algin = "left" vspace = "5" hspace = "7"><p style="font-size: 14px; text-align: center;">Simple linear regression</p></div>
    <div style="width: 565px; min-height: 330px; font-size: 16px; margin: 20px 0;line-height: 1.56;"><b>Regression</b>
    - a way to choose from a family of functions the one that minimizes the loss function. The latter characterizes how much the test function deviates from the values at the specified points. If the points are obtained in an experiment, they inevitably contain measurement error, noise, so it is more reasonable to require that the function conveys the general trend, rather than exactly passing through all the points. In a sense, regression is an "interpolating approximation": we want to draw the curve as close to the points as possible and still keep it as simple as possible to capture the overall trend. The loss function (in English literature, "loss function" or "cost function") is responsible for the balance between these conflicting desires.
</div></div>
<p style="width: 820px; font-size: 16px; line-height: 1.56;"> The purpose of regression is to find the coefficients of this linear combination, and thereby determine the regression function (which is also called the model). I note that linear regression is called linear precisely because of the linear combination of the basis functions f this is not related to the basis functions themselves (they can be linear or not).
</p>
<img style="font-size: 16px; line-height: 1.56;" src="static/res/lingif.gif">
<p style="font-size: 16px; line-height: 1.56;"><a href="https://colab.research.google.com/github/fbeilstein/machine_learning/blob/master/workbook_09_linear_regression.ipynb#scrollTo=JVHnuysdS5fq">You can do it with a demo in Google Co lab.</a>
</p>
</br>
<h2>Quadratic regression</h2>
<div style="display: grid; grid-template-columns: 3fr 1fr; grid-gap: 20px;">
<div style="height: 440px; font-size: 16px; margin: 20px 0;line-height: 1.56;"><p>To assess the ability of an investment manager to correctly choose the time of an operation, it is sometimes necessary to use more complex dependencies than just a straight line to approximate dot diagrams. Let us consider a procedure that allows us to construct the corresponding curve, using statistical methods for estimating the parameters a, b, and c in the following quadratic regression equation</p>
<img style="margin: 20px 0;" src="static/res/form1.png">
<p style="font-size: 16px;line-height: 1.56;">If the estimated value of c is positive, then the slope of the curve decreases when moving from right to left. This means that the portfolio manager has successfully selected the time of the operation. Let us consider how this equation relates to the equation of the a posteriori characteristic line in the case when c is almost zero. In this situation, a and b correspond to the a posteriori' alpha 'and' beta ' of the portfolio.</p></div><div>
<img src="static/res/kvadrat.png" style="margin:20px 0;"><p style="text-align:center;">A Posteriori characteristic curves and straight lines</p></div></div>
</br>
</br>
</br>
</br>
</br>
</div>

