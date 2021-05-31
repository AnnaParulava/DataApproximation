<table>
    <tr>
    <td></td>
    %for i in range(rows):
    <td style="text-align: center">{{i+1}}</td>
    %end
    </tr>
    
    <tr> <td><b>x</b></td>
    %for j in range(rows):
    <td><input type="Number" name="field{{i}}{{j}}" min="0" max="1" placeholder="0"></td>
    %end
    </tr>

    <tr> <td><b>y</b></td>
    %for j in range(rows):
    <td><input type="Number" name="field{{i}}{{j}}" min="0" max="1" placeholder="0"></td>
    %end
    </tr>
    %end
    </table>
<br>