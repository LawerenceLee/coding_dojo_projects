# HTML Notes

## Validating your HTML

Use the link below to check if your HTML is valid (you can paste your code in):

[Nu Html Checker](https://validator.w3.org/nu/#l26c31)

## Meta Tags

Meta tags make your web page more meaningful for search engines like Google.

The attribute content of the description meta tag describes the basic purpose of your web page (a summary of what the web page contains). For each web page, you should place a concise and relevant summary in this section.

For example, this description:

```html
<title>Coding Dojo: Coding Bootcamp in Seattle and San Francisco</title>
<meta name="description" content="Coding Dojo Founder, Michael Choi, developed and refined the dynamic learning curriculum after years of hands-on experience as an executive in fast growing..."><br>copy
```

This is what shows up in Google's search engine results page:

![Coding Dojo Google Search Result](dojo_search.png)

The "Coding Dojo: Coding Bootcamp in Seattle and San Francisco" comes from the `<title>` tag.

* `<meta charset="utf-8">`

Properly encoded Web pages declare the encoding to a browser through a meta tag in the header. Without this tag, a browser may not know to switch to the proper encoding and characters may be displayed as gibberish.

*  `<meta name="description" content="description content">`

The description meta tag is used by search engines when displaying results.

* `<link rel="stylesheet" href="my_css_file.css">`

This line links a stylesheet to our page, which will determine how our HTML elements are visually displayed on the page. We will learn more about what goes into my_css_file.css in the CSS section.

* `<script src="my_javascript_library.js"></script>`

This line links a JavaScript or jQuery file to our document. JavaScript makes our pages interactive. We will learn more about these files in the jQuery section.

NOTE: You can link to as many stylesheets or JavaScript files as you want within the head tags.

***
## Images

There are two ways that we use images on a web page: as `page elements` (such as album art in Pandora, or the photos in your Facebook feed), or as `background images` (this is covered in CSS section).

It has two required attributes: `src` and `alt`.  The `src` attribute stands for source. This is the link to where the image is residing. The alt attribute stands for alternate. This is a few words of text to describe the image, in case it fails to load. This is also used by screen readers, for the vision-impaired. If (and only if) we also specify its `height` and `width attributes`, this text will show up where the image should be in case the image fails to load.

* `<img src="http://....." alt="" height=100 width=100>`

***
## Links

The tag used for links is the `<a>` tag, which stands for the anchor tag. Similar to images, links also need to have an attribute that tells the browser where the link is pointing. For links, this is called the href attribute.

Possible values for the href attribute are:

- An absolute URL - points to another website (like href="http://www.example.com/default.html")
- A relative URL - points to a file within a website (like href="default.html")
- An anchor URL - points to an anchor inside a page (like href="#top")

* `<a href="http://myfakesite.com">LINK TEXT HERE</a>`

***
## Tables

We will often find ourselves using tables to display data. Don't be intimidated by the word "data", it just means information.

Tables have many tags associated with them because they are made up of many different parts. They have:

- A table head (<thead>), which contains rows (<tr>) and column names (<th>).
- A table body (<tbody>), which contains rows (<tr>) filled with table data (<td>).
So the tags we need are:

`<table>, <thead>, <th>, <tbody>, <tr> and <td>`

Example:

```html
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Phone number</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Sample Name</td>
            <td>an_email@gmail.com</td>
            <td>555-5555</td>
        </tr>
        <tr>
            <td>Another Name</td>
            <td>another_email@gmail.com</td>
            <td>444-4444</td>
        </tr>
    </tbody>
</table>
```

The above code displays the following:

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Phone number</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Sample Name</td>
            <td>an_email@gmail.com</td>
            <td>555-5555</td>
        </tr>
        <tr>
            <td>Another Name</td>
            <td>another_email@gmail.com</td>
            <td>444-4444</td>
        </tr>
    </tbody>
</table>

***
## Forms


When the user needs to enter a short amount of text, such as an email address or name.
The appropriate input type here is __text__.

```html
<label for="first_name">First Name:</label>
<input type="text" id="first_name" name="first_name">
<label for="last_name">Last Name:</label>
<input type="text" id="last_name" name="last_name">
<label for="email">Email:</label>
<input type="text" id="email" name="email">
```

<label for="first_name">First Name:</label>
<input type="text" id="first_name" name="first_name">
<label for="last_name">Last Name:</label>
<input type="text" id="last_name" name="last_name">
<label for="email">Email:</label>
<input type="text" id="email" name="email">

__A password field.__

The appropriate input type here is password.

```html
<label for="password">Password</label>
<input type="password" id="password" name="password">
```

<label for="password">Password</label>
<input type="password" id="password" name="password">

When the user can choose only 1 option from a variety of options. A good example is a gender selector.

One appropriate input type here is __radio buttons__.

```html
<label for="male">Male</label>
<input type="radio" id="male" name="gender" value="male">
<label for="female">Female</label>
<input type="radio" id="female" name="gender" value="female">
```

<label for="male">Male</label>
<input type="radio" id="male" name="gender" value="male">
<label for="female">Female</label>
<input type="radio" id="female" name="gender" value="female">

Another option is a __dropdown menu__, which uses `<select>` and `<option>` tags.

```html
<select name="gender">
    <option value="male">Male</option>
    <option value="female">Female</option>
</select>
```

<select name="gender">
    <option value="male">Male</option>
    <option value="female">Female</option>
</select>

When the user can choose multiple things from a variety of options, such as choosing their favorite 3 colors from 5 options.

The appropriate input type here is __checkboxes__.

```html
<label for="blue">Blue</label>
<input type="checkbox" id="blue" name="color" value="blue">
<label for="green">Green</label>
<input type="checkbox" id="green" name="color" value="green">
<label for="red">Red</label>
<input type="checkbox" id="red" name="color" value="red">
<label for="black">Black</label>
<input type="checkbox" id="black" name="color" value="black">
<label for="purple">Purple</label>
<input type="checkbox" id="purple" name="color" value="purple">
copy<div id="copy-toolbar-container" style="cursor: pointer; position: absolute; top: 1230.9998779296875px; right: 35px; padding: 0px 3px; background-color: rgba(224, 224, 224, 0.2); box-shadow: rgba(0, 0, 0, 0.2) 0px 2px 0px 0px; color: rgb(187, 187, 187); border-top-left-radius: 0.5em; border-top-right-radius: 0.5em; border-bottom-right-radius: 0.5em; border-bottom-left-radius: 0.5em; font-size: 0.8em; background-position: initial initial; background-repeat: initial initial;"><span id="copy-toolbar">copy</span></div>
```

<label for="blue">Blue</label>
<input type="checkbox" id="blue" name="color" value="blue">
<label for="green">Green</label>
<input type="checkbox" id="green" name="color" value="green">
<label for="red">Red</label>
<input type="checkbox" id="red" name="color" value="red">
<label for="black">Black</label>
<input type="checkbox" id="black" name="color" value="black">
<label for="purple">Purple</label>
<input type="checkbox" id="purple" name="color" value="purple">
copy<div id="copy-toolbar-container" style="cursor: pointer; position: absolute; top: 1230.9998779296875px; right: 35px; padding: 0px 3px; background-color: rgba(224, 224, 224, 0.2); box-shadow: rgba(0, 0, 0, 0.2) 0px 2px 0px 0px; color: rgb(187, 187, 187); border-top-left-radius: 0.5em; border-top-right-radius: 0.5em; border-bottom-right-radius: 0.5em; border-bottom-left-radius: 0.5em; font-size: 0.8em; background-position: initial initial; background-repeat: initial initial;"><span id="copy-toolbar">copy</span></div>

When the user might want to enter longer text. This can be used in forums for comments, or for user profile descriptions.

__In this case we use the `<textarea>` tag.__

`<textarea name="description"></textarea>`

<textarea name="description"></textarea>

When a form needs to submit more than just user input. 
__Input type hidden__ is similar to text fields, except they do not show on the page and users can not enter anything into them. This is useful for the back-end authentication and passing data. 

```html
<input type="hidden" name="id" value="7">
```

Finally, to create a submit button:
The appropriate input type is __submit__.

```html
<input type="submit" value="Submit">
```

<input type="submit" value="Submit">

Let's look at a sample full registration form:

```html
<form action="process.php" method="post">
    <p>Please Register</p>
    <label for="first_name">First Name:</label>
    <input type="text" id="first_name" name="first_name">
   
    <label for="last_name">Last Name:</label>
    <input type="text" id="last_name" name="last_name">
   
    <label for="email">Email:</label>
    <input type="text" id="email" name="email">
   
    <p>Select your gender:</p>
    <label for="male">Male</label>
    <input type="radio" id="male" name="gender" value="male">
   
    <label for="female">Female</label>
    <input type="radio" id="female" name="gender" value="female">
   
    <p>Select 3 of your favorite colors:</p>
    <label for="blue">Blue</label>
    <input type="checkbox" id="blue" name="color" value="blue">
    
    <label for="green">Green</label>
    <input type="checkbox" id="green" name="color" value="green">
   
    <label for="red">Red</label>
    <input type="checkbox" id="red" name="color" value="red">
    
    <label for="black">Black</label>
    <input type="checkbox" id="black" name="color" value="black">
   
    <label for="purple">Purple</label>
    <input type="checkbox" id="purple" name="color" value="Purple">
    
    <p>Say a few words about yourself:</p>
    <textarea name="description"></textarea>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password">
   <label for="pw_confirm">Password Confirmation:</label>
   <input type="password" id="pw_confirm" name="password_confirmation">
   
   <input type="submit" value="Click here to register">
</form>
```

<form action="process.php" method="post">
    <p>Please Register</p>
    <label for="first_name">First Name:</label>
    <input type="text" id="first_name" name="first_name">
    <label for="last_name">Last Name:</label>
    <input type="text" id="last_name" name="last_name">
    <label for="email">Email:</label>
    <input type="text" id="email" name="email">
    <p>Select your gender:</p>
    <label for="male">Male</label>
    <input type="radio" id="male" name="gender" value="male">
    <label for="female">Female</label>
    <input type="radio" id="female" name="gender" value="female">
    <p>Select 3 of your favorite colors:</p>
    <label for="blue">Blue</label>
    <input type="checkbox" id="blue" name="color" value="blue">
    <label for="green">Green</label>
    <input type="checkbox" id="green" name="color" value="green">
    <label for="red">Red</label>
    <input type="checkbox" id="red" name="color" value="red">
    <label for="black">Black</label>
    <input type="checkbox" id="black" name="color" value="black">
    <label for="purple">Purple</label>
    <input type="checkbox" id="purple" name="color" value="Purple">
    <p>Say a few words about yourself:</p>
    <textarea name="description"></textarea>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password">
   <label for="pw_confirm">Password Confirmation:</label>
   <input type="password" id="pw_confirm" name="password_confirmation">
   <input type="submit" value="Click here to register">
</form>
Other label-input Declaration

Most CSS frameworks (especially on Twitter Bootstrap), use the label-input pairing shown above, but you may encounter a different format on how the label-input set is being declared. Below is an example:

```html
<form>    
    <p>Please Register</p>
    <label>
        Name:<input type="text" name="name">
    </label>
    <p>Select your gender:</p>
    <label>
       Male<input type="radio" name="gender" value="male"> 
    </label>
    <label>
       Female<input type="radio" name="gender" value="female">
    </label>
    <p>For security, enter your password.</p>
    <label>
        Password:<input type="password" name="password">
    </label>
    <input type="submit" value="Click here to register">
</form>
```

<form>    
    <p>Please Register</p>
    <label>
        Name:<input type="text" name="name">
    </label>
    <p>Select your gender:</p>
    <label>
       Male<input type="radio" name="gender" value="male"> 
    </label>
    <label>
       Female<input type="radio" name="gender" value="female">
    </label>
    <p>For security, enter your password.</p>
    <label>
        Password:<input type="password" name="password">
    </label><br>
    <input type="submit" value="Click here to register">
</form>

Notice that the input element is now nested inside the label element and we no longer need to link the two using the label's for attribute and the input's id attribute.


If you encounter the following error:

`The for attribute of the label element must refer to a non-hidden form control`

Here's the fix given by <a href="https://stackoverflow.com/questions/18945774/validating-html-the-for-attribute-of-the-label-element-must-refer-to-a-form-con">Stackoverflow</a>:

If you use the for attribute in a label element it has to match the id of an input element in your form.

```html
<label for="field-id" style="line-height:24px;">Your Name</label><br>&nbsp;&nbsp;
<input type="text" id="field-id">
```

***
## Div & Span

Div Element `<div></div>`: Block level elements that allow you to group content that belongs together into a container.

Span Element `<span></span>`: Inline elements that work like the div element, but are meant for smaller bits of information (e.g. Pieces of text inside a paragraph).

***
## HTML5 Tag Conventions

* __DOCTYPE__: `<!DOCTYPE html>`
* __Character Encoding__: `<meta charset="utf-8">`
* __Scripts__: `<script src="main.js"></script>`
* __Links__: `<link rel="stylesheet" href="style.css">`

***
## Rich Media

### Cavnas Element

The HTML `<canvas>` element is used to draw graphics, on the fly, via JavaScript. The `<canvas>` element is only a container for graphics. You must use JavaScript to actually draw the graphics. Canvas has several methods for drawing paths, boxes, circles, text, and adding images.

Draw a Line w/ JS inside a Canvas Element:

```html
<canvas id="myCanvas" width="200" height="100" style="border:1px solid #d3d3d3;">
Your browser does not support the HTML5 canvas tag.</canvas>

<script>
var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
ctx.moveTo(0,0);
ctx.lineTo(200,100);
ctx.stroke();
</script>
```

<canvas id="myCanvas" width="200" height="100" style="border:1px solid #d3d3d3;">
Your browser does not support the HTML5 canvas tag.</canvas>

<script>
    var c = document.getElementById("myCanvas");
    var ctx = c.getContext("2d");
    ctx.moveTo(0,0);
    ctx.lineTo(200,100);
    ctx.stroke();
</script>

### Audio Element

Embedding an audio file in an HTML5 document is simple:

```html
<audio src="desperado.mp3">
</audio>
```

__Autoplay Attribute__

*The autoplay attribute does not work in mobile devices like iPad and iPhone.*

```html
<audio src="desperado.mp3" autoplay>
</audio>
```

__Autoplay & Loop Attribute__

```html
<audio src="desperado.mp3" autoplay loop>
</audio>
```

__Playback Controls__

```html
<audio src="desperado.mp3" controls>
</audio>
```

#### The problem with MP3's...

`MP3` format is widely used everywhere, but it is not an open format. This means is that browsers can't decode MP3 files without paying a fee. `OGG` files are the open format version of MP3, sadly it is not supported by all browsers either.


#### Browser Support
<table>
    <thead>
        <tr>
            <th style="width:25%">Browser</th>
            <th style="width:25%">MP3</th>
            <th style="width:25%">Wav</th>
            <th style="width:25%">Ogg</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Internet Explorer</td>
            <td>YES</td>
            <td>NO</td>
            <td>NO</td>
        </tr>
        <tr>
            <td>Chrome</td>
            <td>YES</td>
            <td>YES</td>
            <td>YES</td>
        </tr>
        <tr>
            <td>Firefox</td>
            <td>YES</td>
            <td>YES</td>
            <td>YES</td>
        </tr>
        <tr>
            <td>Safari</td>
            <td>YES</td>
            <td>YES</td>
            <td>NO</td>
        </tr>
        <tr>
            <td>Opera</td>
            <td>YES</td>
            <td>YES</td>
            <td>YES</td>
        </tr>
    </tbody>
</table>

#### MIME Types for Audio Formats

<table class="w3-table-all notranslate" id="table2">
    <thead>
        <tr>
        <th style="width:50%">Format</th>
        <th style="width:50%">MIME-type</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>MP3</td>
            <td>audio/mpeg</td>
        </tr>
        <tr>
            <td>Ogg</td>
            <td>audio/ogg</td>
        </tr>
        <tr>
            <td>Wav</td>
            <td>audio/wav</td>
        </tr>
    </tbody>
</table>

A browser that can play back Ogg Vorbis files will look no further than the first source element. A browser that can play MP3 files will skip over the first source element and play the file in the second source element.

```html
<audio controls>
    <source src="desperado.ogg">
    <source src="desperado.mp3">
</audio>
```

### Video Element

Works much like the audio element (e.g. autoplay, controls, etc.), but you'll want to include dimensions for this element.

*The autoplay attribute does not work in mobile devices like iPad and iPhone.*

```html
<video src="caddyshack.mp4" width="400" height="800" controls>
</video>
```

Also like the audio element there is a battle for dominance regarding format. 

#### Browser Support 

<table class="w3-table-all notranslate">
<thead>
    <tr>
        <th style="width:25%">Browser</th>
        <th style="width:25%">MP4</th>
        <th style="width:25%">WebM</th>
        <th style="width:25%">Ogg</th>
    </tr>
</thead>
<tbody>
<tr>
<td>Internet Explorer</td>
<td>YES</td>
<td>NO</td>
<td>NO</td>
</tr>
<tr>
<td>Chrome</td>
<td>YES</td>
<td>YES</td>
<td>YES</td>
</tr>
<tr>
<td>Firefox</td>
<td>YES</td>
<td>YES</td>
<td>YES</td>
</tr>
<tr>
<td>Safari</td>
<td>YES</td>
<td>NO</td>
<td>NO</td>
</tr>
<tr>
<td>Opera</td>
<td>YES (from Opera 25)</td>
<td>YES</td>
<td>YES</td>
</tr>
</tbody></table>

#### HTML Video - Media Types

<table class="w3-table-all notranslate" id="table1">
<thead>
    <tr>
        <th style="width:50%">File Format</th>
        <th style="width:50%">Media Type</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>MP4</td>
        <td>video/mp4</td>
    </tr>
    <tr>
        <td>WebM</td>
        <td>video/webm</td>
    </tr>
    <tr>
        <td>Ogg</td>
        <td>video/ogg</td>
    </tr>
</tbody></table>

*MP4 is patent-encumbered*

Use can use the video element like the audio element to have your video play on all browser that support the video element (see above for details).

```html
<video width="400" height="200" poster="picture.jpg" controls>
    <source src="caddyshack.ogv">
    <source src="movie.mp4">
</video>
```

One of the limitations of relying on a plug-in for rich media is that plug-in content is sandboxed away from the rest of the web page. Having native rich media elements in HTML means that we can have our media content play nicely with other browser technologies such as CSS and JavaScript.

## Difference between `id` and `name` attributes

The `id` attribute identifies your element for the front-end (CSS and JavaScript.) It can be used on ANY element.

The `name` attribute belongs ONLY on form elements and is used in the back-end (PHP, Ruby on Rails, etc.) to identify your form's values.

## What is the DOM?

### Definition
The Document Object Model (DOM) is a structured representation of your HTML as generated by the browser, allowing access to the elements of your web page so they may be manipulated. Generally, it is JavaScript that does this manipulation. The DOM is notoriously hard to define, so here's a metaphor:

### Metaphor
Let's say we have a piece of paper that says "Coding Dojo Rocks!". We take out some magnetic letters, go to our fridge, and write out "Coding Dojo Rocks!", as per our paper. That paper is your HTML, and the magnets can be considered our DOM.

In a lot of cases, the magnets will remain the same as what is written on our paper, so there will be almost no difference between HTML and the DOM. In other cases, we will want to change the words on the fridge, or alter the color of the magnets, or add other neat functionality. Changing those things is manipulating the DOM; the HTML paper we started with is unchanged, but the DOM is no longer identical

### Explaination of Metaphor
When you see JavaScript that changes the DOM or hear people talking about DOM manipulation, they are basically talking about interacting with those fridge magnets, after they had copied off of our HTML paper.