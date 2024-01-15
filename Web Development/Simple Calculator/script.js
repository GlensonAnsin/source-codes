function calculate() {
    var num1 = parseFloat(document.getElementById("input1").value);
    var num2 = parseFloat(document.getElementById("input2").value);

    if (isNaN(num1) || isNaN(num2)) {
        alert("Please enter valid numbers");
        return;
    }

    document.getElementById("sum").innerText = num1 + num2;
    document.getElementById("difference").innerText = num1 - num2;
    document.getElementById("product").innerText = num1 * num2;

    if (num2 !== 0) {
        document.getElementById("quotient").innerText = num1 / num2;
    } else {
        document.getElementById("quotient").innerText = "Undefined (division by zero)";
    }
}