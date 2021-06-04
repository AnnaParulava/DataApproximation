
<table>
    <tr>
    %if len(x)!=0:
    
    </tr>

    <tr> <td style="text-align: center;"><b>x</b></td>
    %for x in x:
    <td><input type="Number" name="fieldX{{x}}" min="0" max="1000" placeholder={{x}} readonly></td>
    %end
    </tr>

    <tr> <td style="text-align: center;"><b>y</b></td>
    %for y in y:
    <td><input type="Number" name="fieldY{{y}}" min="0" max="1000" placeholder={{y}} readonly></td>
    %end
    </tr>
    %end
    </table>
<br>