<script>
import axios from 'axios';

export default {
  data() {
    return {
      aboutMe: ''  // Переменная для хранения информации
    };
  },
  mounted() {
    this.fetchAboutMe();  // Вызов функции для получения данных
  },
  methods: {
    async fetchAboutMe() {  // Добавляем async
      try {
        const response = await axios.get('http://127.0.0.1:8000/aboutme');  // Добавляем await
        this.aboutMe = response.data.text;  // Сохраняем полученные данные
        localStorage.setItem("aboutMe", this.aboutMe)
      } catch (error) {
        alert('Ошибка при получении данных: ' + error);  // Исправляем вывод ошибки
      }
    }
  }
}
</script>

<template>
  <div class="about-me">

    <a class="href" href="#paragraph1">Обо мне</a> | <a class="href" href="#paragraph2">Параграф 2</a>
     | <a class="href" href="#paragraph3">Параграф 3</a> | <a class="href" href="#paragraph4">Параграф 4</a>

    <h2 id="paragraph1">Обо мне</h2>
    <hr style="margin-top: 10px; margin-bottom: 10px;"/>

    <p>{{ aboutMe }}</p>  <!-- Выводим информацию -->

    <p>Форматирование в <mark>HTML5</mark></p>
        <img src="../../persiki.jpg" alt="Persiki" style="float:left; width: 30%; margin: 10px;"/>
        <p>Это <b>выделенный</b> текст</p>
        <p>Это <strong>важный</strong> текст</p>
        <p>Это <del>зачеркнутый</del> текст</p>
        <p>Это <s>недействительный</s> текст</p>
        <p>Это <em>важный</em> текст</p>
        <p>Это текст <i>курсивом</i> </p>
        <p>Это <ins>добавленный</ins> текст</p>
        <p>Это <u>подчеркнутый</u> текст</p>
        <p>X<sub>i</sub> = Y<sup><small>2</small></sup> + Z<sup><small>2</small></sup></p>

        <hr style="margin-top: 10px; margin-bottom: 10px;"/>
        <br/>

        <figure style="text-align: center;">
            <figcaption>Февраль 2013</figcaption>
            <img src="../../ava.jpg" style="width: 30%; margin: 10px;">
        </figure>

        <hr style="margin-top: 10px; margin-bottom: 10px;"/>

        <h2 id="paragraph2">Нумерованный список</h2>
        <ol>
            <li>iPhone 6S</li>
            <li>Galaxy S7</li>
            <li>Nexus 5X</li>
            <li>Lumia 950</li>
        </ol>
        <h2 id="paragraph3">Ненумерованный список</h2>
        <ul>
            <li>iPhone 6S</li>
            <li>Galaxy S7</li>
            <li>Nexus 5X</li>
            <li>Lumia 950</li>
        </ul>

        <details>
            <summary>Флагманы 2015</summary>
            <ul>
                <li>iPhone 6S Plus</li>
                <li>Nexus 6P</li>
                <li>Galaxy S6 Edge</li>
                <li>Lumia 950 XL</li>
            </ul>
        </details>

        <hr style="margin-top: 10px; margin-bottom: 10px;"/>

        <table>
          <caption id="paragraph4">Популярные смартфоны 2015</caption>
            <thead>
                <tr>
                    <th>Модель</th> <th>Компания</th> <th>Цена</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Nexus 6P</td> <td>Huawei</td> <td>49000</td>
                </tr>
                <tr>
                    <td>iPhone 6S PLus</td> <td>Apple</td> <td>62000</td>
                </tr>
                <tr>
                    <td>Lumia 950 XL</td> <td>Microsoft</td> <td>35000</td>
                </tr>
            </tbody>
            <tfoot>
                <tr>
                    <th colspan="3">Информация по состоянию на 17 марта</th>
                </tr>
            </tfoot>
        </table>

        <hr style="margin-top: 10px; margin-bottom: 10px;"/>
        <a class="href" href="http://metanit.com/web/html5/" target="_blank">Учебник по HTML5</a> <br/>
        <!-- _blank - открытие в новой вкладке -->
         
        <div style="text-align: center;">
        <iframe src="http://wikipedia.com" width="1000" height="500">
        </iframe></div>
  </div>

  <hr style="margin-top: 10px; margin-bottom: 10px;"/>

    <form>
        <p><input list="phonesList" type="text" name="model" placeholder="Введите модель" /></p>
        <p>
            <button type="submit">Отправить</button>
        </p>
    </form>

    <datalist id="phonesList">
        <option value="iPhone 6S" label="54000"/>
        <option value="Lumia 950">35000</option>
        <option value="Nexus 5X"/>
    </datalist>

    <hr style="margin-top: 10px; margin-bottom: 10px;"/>

    <form>
        <input type="search" name="term" />
        <input type="submit" value="Поиск" />
    </form>

    <hr style="margin-top: 10px; margin-bottom: 10px;"/>

    <form>
        <p>
            <label for="login">Логин: </label>
            <input type="text" autocomplete="off" autofocus="on" id="login" name="login" />
        </p>
        <p>
            <label for="password">Пароль: </label>
            <input type="password" autocomplete="off" id="password" name="password" />
        </p>
        <p>
            <button type="submit">Отправить</button>
        </p>
    </form>

    <hr style="margin-top: 10px; margin-bottom: 10px;"/>

    <form>
        <p>
            <label for="price">Цена: </label>
            <input type="number" list="priceList"
                step="1000" min="3000" max="100000" value="" id="price" name="price"/>
        </p>
        <p>
            <button type="submit">Отправить</button>
        </p>
    </form>

    <datalist id="priceList">
        <option value="15000" />
        <option value="20000" />
        <option value="25000" />
    </datalist>

    <hr style="margin-top: 10px; margin-bottom: 10px;"/>

    <p>
        <label for="price">Цена:</label> 
        1<input type="range" step="1" min="0" max="100" value="50" id="price" name="price"/>100
    </p>

    <hr style="margin-top: 10px; margin-bottom: 10px;"/>

    <form>
        <p><input type="checkbox" checked name="html5"/>HTML5</p>
        <p><input type="checkbox" name="dotnet"/>.NET</p>
        <p><input type="checkbox" name="java"/>Java</p>
        <p>
            <button type="submit">Отправить</button>
        </p>
    </form>

    <hr style="margin-top: 10px; margin-bottom: 10px;"/>

    <form>
        <h2>Укажите пол</h2>
        <p>
            <input type="radio" value="man" checked name="gender"/>мужской
        </p>
        <p>
            <input type="radio" value="woman" name="gender"/>женский
        </p>
        <h2>Выберите технологию</h2>
        <p>
            <input type="radio" value="html5" checked name="tech"/>HTML5
        </p>
        <p>
            <input type="radio" value="net" name="tech"/>.NET
        </p>
        <p>
            <input type="radio" value="java" name="tech"/>Java
        </p>
        <p>
            <button type="submit">Отправить</button>
        </p>
    </form>

    <hr style="margin-top: 10px; margin-bottom: 10px;"/>

    <label for="favcolor">Выберите цвет</label>
    <input type="color" id="favcolor" name="favcolor" />

    <hr style="margin-top: 10px; margin-bottom: 10px;"/>

    <label for="favcolor">Выберите цвет</label>
    <input type="color" list="colors" id="favcolor" name="favcolor" />
    <datalist id="colors">
        <option value="#0000FF" label="blue"/>
        <option value="#008000" label="green"/>
        <option value="#ff0000" label="red"/>
    </datalist>

    <hr style="margin-top: 10px; margin-bottom: 10px;"/>

    <form>
        <p>
            <label for="email">Email: </label>
            <input type="email" placeholder="user@gmail.com" id="email" name="email"/>
        </p>
        <p>
            <label for="url">URL: </label>
            <input type="url" id="url" name="url"/>
        </p>
        <p>
            <label for="phone">Телефон: </label>
            <input type="phone" pattern="\+\d-\d{3}-\d{3}-\d{4}" placeholder="+X-XXX-XXX-XXXX" id="phone" name="phone"/>
            <!-- formnovalidate - для отключения валидации  -->
        </p>
        <p>
            <button type="submit">Отправить</button> 
        </p>
    </form>

    <hr style="margin-top: 10px; margin-bottom: 10px;"/>

    <form>
        <p>
            <label for="date">Дата рождения: </label>
            <input type="date" id="date" name="date"/>
        </p>
        <p>
            <button type="submit">Отправить</button>
        </p>
     </form>

     <form>
        <p>
            <label for="week">Неделя: </label>
            <input type="week" name="week" id="week" />
        </p>
        <p>
            <label for="localdate">Дата и время: </label>
            <input type="datetime-local" id="localdate" name="date"/>
        </p>
        <p>
            <label for="month">Месяц: </label>
            <input type="month" id="month" name="month"/>
        </p>
        <p>
            <label for="time">Время: </label>
            <input type="time" id="time" name="time"/>
        </p>
        <p>
            <button type="submit">Отправить</button>
        </p>
    </form>

     <hr style="margin-top: 10px; margin-bottom: 10px;"/>

     <!-- <form enctype="multipart/form-data" method="post" action="http://localhost:8080/postfile.php"> -->
    <form>
        <p>
            <input type="file" accept=".jpg" multiple required name="file" />
        </p>
        <p>
            <input type="submit" value="Отправить" />
        </p>
    </form>

    <hr style="margin-top: 10px; margin-bottom: 10px;"/>

    <form method="get">
        <p>
            <select multiple id="phone" name="phone">

                <option value="iphone 6s">iPhone 6S</option>
                <option value="lumia 950">Lumia 950</option>
                <option value="nexus 5x" selected>Nexus 5X</option>
                <option value="galaxy s7">Galaxy S7</option>
            </select>

            <select multiple id="phone" name="phone">
                <optgroup label="Apple">
                    <option value="iphone 6s">iPhone 6S</option>
                    <option value="iphone 6s plus">iPhone 6S Plus</option>
                    <option value="iphone 5se">iPhone 5SE</option>
                </optgroup>
                <optgroup label="Microsoft">
                    <option value="lumia 950">Lumia 950</option>
                    <option value="lumia 950 xl">Lumia 950 XL</option>
                    <option value="lumia 650">Lumia 650</option>
                </optgroup>
            </select>
        </p>
        <p>
            <input type="submit" value="Отправить" />
        </p>
    </form>

    <hr style="margin-top: 10px; margin-bottom: 10px;"/>

    <textarea class="comment" id="comment" name="comment" placeholder="Написать комментарий"></textarea> 

    <form>
        <fieldset>
            <legend>Введите данные:</legend>
            <label for="login">Логин:</label><br>
            <input type="text" name="login" id="login" /><br>
            <label for="password">Пароль:</label><br>
            <input type="password" name="password" id="password" /><br>
            <input type="submit" value="Авторизация">
        </fieldset>
    </form> 


</template>

<style>
  .href:link {color:rgb(0, 255, 102); text-decoration:none}
  .href:visited {color:rgb(255, 0, 43); text-decoration:none}
  .href:hover   {color:rgb(220, 80, 255); text-decoration:underline; background-color: #252525;}
  .href:active  {color:yellow; text-decoration:underline}
  input[type="range"] {width: 50%; margin: 10px;}
  .comment {
    width: 30%;
    height: 20%;
    resize: none;
  }
  
</style>