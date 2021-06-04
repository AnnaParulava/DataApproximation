 
<table>
    <tr>
    
    %for i in range(row):
    <td style="text-align: center">{{i+1}}</td>
    %end
    </tr>

    <tr> <td style="text-align: center;"><b>x</b></td>
    %for j in range(rows):
    <td><input type="Number" step="0.01" name="fieldX{{j}}" min="0" max="1000" placeholder="0"></td>
    %end
    </tr>

    <tr> <td style="text-align: center;"><b>y</b></td>
    %for j in range(rows):
    <td><input type="Number" step="0.01" name="fieldY{{j}}" min="0" max="1000" placeholder="0"></td>
    %end
    </tr>
    %end
    </table>
<br> 