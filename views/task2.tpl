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

    <h2 style="margin: 90px 0 30px 0;">Function approximation</h2>
    <div style="display: grid; grid-template-columns: 1fr 3fr;"><div><img style="" src="static\res\linar.png" width="300" algin = "left" vspace = "5" hspace = "7"><p style="font-size: 14px; text-align: center;">Simple linear regression</p></div>
    <div style="width: 565px; min-height: 330px; font-size: 16px; margin: 20px 0;line-height: 1.56;">&nbsp;&nbsp;In general <b>function approximation</b>
    problem asks us to select a function among a well-defined class that closely matches ("approximates") a target function in a task-specific way. 
    The need for function approximations arises in many branches of applied mathematics, and computer science in particular.
    One can distinguish two major classes of function approximation problems:<br>
    &nbsp;&nbsp;First, for known target functions approximation theory is the branch of numerical analysis that investigates how certain known functions can be approximated by a specific class of functions that often have desirable
    properties. <br>&nbsp;&nbsp;Second, the target function, call it g, may be unknown; instead of an explicit formula, 
    only a set of points of the form (x, g(x)) is provided. <br>&nbsp;&nbsp;To some extent, the different problems (regression, classification, fitness approximation)
    have received a unified treatment in statistical learning theory, where they are viewed as supervised learning problems.</div>
    </div>

</br>
<h2>Quadratic regression line coefficients</h2>
<div style="display: grid; grid-template-columns: 3fr 1fr; grid-gap: 20px;">
<div style="height: 440px; font-size: 16px; margin: 20px 0;line-height: 1.56;"><p>To find the coefficients a1, a2 and a3 by the least squares method, it is necessary to solve the system of equations:</p>
<img style="margin: 20px 0;" src="static/res/regr.png">
<p style="font-size: 16px;line-height: 1.56;">To calculate R2, we use the formula:</p>
<img style="margin: 20px 0;" src="static/res/r.png"></div>
<div>
<img src="static/res/12.gif" style="margin:20px 0;"><p style="text-align:center;">...</p></div></div>
</br>
</br>
</br>
</br>
</br>
</br>
</br>
</br>
</div>

