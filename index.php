<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="UTF-8">
    <!-- <meta http-equiv="refresh" content="1"; URL="http://localhost/index.php"> -->
    <!-- <link href="home.css" rel="stylesheet" type="text/css"> -->
    <link id="PageStyleSheet" rel="stylesheet" href="home.css" />
    <title>Document</title>
  </head>
  <body>
    <script>
    function clickBtn1(){
    	const color1 = document.form1.color1;
    	// 値(数値)を取得
    	const num = color1.selectedIndex;
    	//const num = document.form1.color1.selectedIndex;
    	// 値(数値)から値(value値)を取得
    	const str = color1.options[num].value;
    	//const str = document.form1.color1.options[num].value;
    	document.getElementById("span1").textContent = str;
    }
    </script>



    <?php
if(isset($_POST["fruits"])) {
  // セレクトボックスで選択された値を受け取る
  $fruit = $_POST["fruits"];

  // 受け取った値を画面に出力
  $start = microtime();
  // echo $start;
  echo shell_exec("export LANG=ja_JP.UTF-8; python3 writing.py ".$fruit);

  $i = 0; //初期化する
  while(true){
      // echo $i;
      $i += 1;
      $now = microtime();
      // echo $now;
      $gap = $now - $start;
      // echo $gap;
      echo "<br>"; //改行
      if(1 < $gap){
        echo $gap;
        break;
      }
  }
    // $now = time();
    // $gap = $now - $start;
    // echo $gap;
  }
?>

    <br>
    <br>
    <br>
    <form action="index.php" method = "POST">
        <select name= "fruits">
          <option value = "" selected></option>
          <option value = "black">BLACK</option>
          <option value = "blue">BLUE</option>
          <option value = "red">RED</option>
          <option value = "green">GREEN</option>
          <option value = "purple">PURPLE</option>
          <option value = "yellow">YELLOW</option>
        </select>
        <input type="submit"name="submit"value="送信"/>
      </form>
      <br>
      <br>
      <br>
    <div class="main">
      <div class="graph1">
        <img class="circle1" src="./population.png">
        <!-- <img class="circle2" src="./population.png"> -->
      </div>
      <hr>
      <div class="graph2">
        <!-- <img class="circle1" src="./population.png">
        <img class="circle2" src="./population.png"> -->
      </div>
    </div>

  </body>
</html>
