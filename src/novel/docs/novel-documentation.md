Introduction
------------

This style-pack gives you some additional ways to format your text, so
that you can easily produce books for print and e-Readers.

Formating
---------

### Usage

Markdown is used to format the book. You can use all functionality
provided by [pandocs
markdown](http://pandoc.org/MANUAL.html#pandocs-markdown). But while
markdown excels at light markup, sometimes you need special formatting.
Poems, epigraphs etc. are good examples. To make formatting these
elements easy, this template comes with an easy to use syntax for many
such elements. Each of this styles comes with one or more filters, which
formats these elements according to the output format.

The syntax is very easy. Either

**Div-Syntax**

    :::{.type .option key=value}
    The content that should be styled.
    :::

or

**Code-Block-Syntax**

    ~~~{.type .option key=value}
    The content that should be styled.
    ~~~

depending on the style used.

Types and simple options are preceded by a dot, attributes consist of a
name and a value. These options are separated by a simple space. If the
value of an attribute contains spaces, you need to surround it with
quotation marks.

For example, this is how you would implement a poem:

    ~~~{.poem author="William Shakespeare" title="Sonnet 18"}
    Shall I compare thee to a summer's day?
    Thou art more lovely and more temperate:
    Rough winds do shake the darling buds of May,
    And summer's lease hath all too short a date:

    Sometime too hot the eye of heaven shines,
    And often is his gold complexion dimmed,
    And every fair from fair sometime declines,
    By chance, or nature's changing course untrimmed:

    But thy eternal summer shall not fade,
    Nor lose possession of that fair thou ow'st,
    Nor shall death brag thou wand'rest in his shade,
    When in eternal lines to time thou grow'st,

    |       So long as men can breathe or eyes can see,
    |       So long lives this, and this gives life to thee.
    ~~~

And this is what it looks rendered:

``` {.poem author="William Shakespeare" title="Sonnet 18"}
Shall I compare thee to a summer's day?
Thou art more lovely and more temperate:
Rough winds do shake the darling buds of May,
And summer's lease hath all too short a date:

Sometime too hot the eye of heaven shines,
And often is his gold complexion dimmed,
And every fair from fair sometime declines,
By chance, or nature's changing course untrimmed:

But thy eternal summer shall not fade,
Nor lose possession of that fair thou ow'st,
Nor shall death brag thou wand'rest in his shade,
When in eternal lines to time thou grow'st,

|       So long as men can breathe or eyes can see,
|       So long lives this, and this gives life to thee.
```

### Some additional Tips

You can use html style comments in your source files.

    <!-- This is a comment. -->

You can add a curly bracket with ".unnumbered" or "-" inside it at the
end of a heading, to exclude it from the automatic numbering, if you
chose to use that.

    # Example Heading{.unnumbered}
    # Example Heading{-}

Metadata options
----------------

You can modify many things about the output in the metadata of your
book.

Two special fields are introduced with this project:

### copyrights

You enter your copyrights text in this field.

### dedication

If your book contains a dedication, enter it in this field.

### Example metadata block

``` {.yaml}
---
title: Alice's Adventures in Wonderland
author: Lewis Carroll
lang: en
copyrights: This book is in the public domain.
dedication: for Elise
poem-style: top
quote-style: top

# epub-cover
cover-image: ./images/cover.jpg

# pdf options
paper: 6in:9in
BCOR: 2mm
fontsize: 12pt
mainfont:
sansfont:

output-name: Alices_Adventures_in_Wonderland
destination: ./dist
formats:
  - html
  - epub
  - pdf
style-file: ~/novel.yaml
---
```

List of styles
--------------

Below you find a description of each type provided with the template and
which filter is used to render it. If no filter is given, it is named
like the style. Some styles have options how they should look in the
rendered book. You can change these in the metadata of your book.

Most styles use the **Div-Syntax**. If no syntax is given, use that
syntax. If they use the **Code-Block-Syntax** this is explicitly stated.

### align\_center, align\_right, align\_left

Text gets aligned accordingly inside the block.

### epigraph

Adds an epigraph.

Attributes:

-   author: The author of the epigraph

### new\_scene

This style is an exception to all others. To make a new scene, just
enter three '\*' on one line surrounded by blank lines. Please note,
that this overrides one default markdown command for a horizontal line.
Just use `---` for horizontal lines.

Example:

    The last paragraph in the old scene.

    * * *

    The first paragraph in the new scene.

Render Options:

-   default: A new scene is marked by blank space

-   text: A new scene is marked by the text given, defaults to `* * *`

-   fleuron: A new scene is marked by an image. You need to provide an
    image in the options

### noindent

The paragraph is not indented.

### poem

Uses the **Code-Block-Syntax**

Styles the content as a poem. There are three render options for this
style, each just formatting the poem slightly different.

Render Options:

-   bottom: Title and author are positioned on the bottom right of the
    poem

-   one-line: As above, but title and author appear on one line

-   top: This filter inserts the title at the top of the poem

Options:

-   altverse: This option indents every other line in a stanza

-   top: Positions the title on the top, regardless of the render option
    used

-   bottom: Positions the title on the bottom, regardless of the render
    option used

-   one-line: Positions author and title in one line on the bottom,
    regardless of the render option used

-   noversewidth: Per default the filter calculates the best position
    for the poem. If you don't want this, use this option

Attributes:

author
:   The author of the poem

title
:   The title of the poem

poemlines
:   Needs a number. Adds a line number every number of lines

versewidth
:   Needs a line of the poem, used to position the poem. Normally this
    is calculated automatically, use this, if you want to set it
    manually

### quote

Styles the content as a quote. Of course markdown has its own syntax for
quotes. You only need this style, if you want to include an author
and/or a title.

There are three render options for this style, each just formating the
quote slightly different.

Render Options:

-   bottom: Title and author are positioned on the bottom right of the
    quote

-   one-line: As above, but title and author appear on one line

-   top: This filter inserts the title at the top of the quote

Options:

-   top: Positions the title on the top, regardless of the render option
    used

-   bottom: Positions the title on the bottom, regardless of the render
    option used

-   one-line: Positions author and title in one line on the bottom,
    regardless of the render option used

Attributes:

-   author: The author of the quote

-   title: The title of the quote
