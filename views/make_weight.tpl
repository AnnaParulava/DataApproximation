<table>
    <tr>
    <td></td>
    %for i in range(rows):
    <td>node {{i+1}}</td>
    %end
    </tr>
    %for i in range(rows):
    <tr> <td>node {{i+1}}</td>
    %end
    %for j in range(rows):
    <td><input type="Number" name="field{{j}}" min="0" max="99" placeholder="0"></td>
    <td><input type="Number" name="field{{j}}" min="0" max="99" style="background-color: #606060" readonly></td>
    %end
    </tr>
    </table>
<br>
