
<table>
    <tr>
    %if len(x)!=0:
    <td></td>
    %for i in range(row):
    <td style="text-align: center">{{i+1}}</td>
    %end
    </tr>

    <tr> <td><b>x</b></td>
    %for x in x:
    <td><input type="Number" name="fieldX{{x}}" min="0" max="1000" placeholder={{x}} readonly></td>
    %end
    </tr>

    <tr> <td><b>y</b></td>
    %for y in y:
    <td><input type="Number" name="fieldY{{y}}" min="0" max="1000" placeholder={{y}} readonly></td>
    %end
    </tr>
    %end
    </table>
<br>