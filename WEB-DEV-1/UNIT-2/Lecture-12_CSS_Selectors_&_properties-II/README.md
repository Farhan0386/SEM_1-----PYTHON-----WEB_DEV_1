# 📘 Lecture 12: CSS Selectors & Properties – II

This session builds upon the foundational CSS concepts introduced in Lecture 11. It focuses on **Attribute Selectors** and **Combinator Selectors**, which allow for more precise and contextual styling of HTML elements.

---

## 🧠 What You’ll Learn

- How to style elements based on their attributes (e.g., `type`, `href`, `alt`)
- How to target elements based on their relationship to other elements in the DOM
- Real-world examples and coding exercises to reinforce each concept

---

## 🧩 Topics Covered

### 1. ✅ Attribute Selectors

Attribute selectors allow you to style HTML elements based on the presence or value of their attributes.

#### 🔹 Syntax Variants

| Selector Type                  | Syntax Example                      | Description                                 |
|-------------------------------|-------------------------------------|---------------------------------------------|
| Attribute exists              | `element[attribute]`                | Selects elements with the attribute         |
| Exact match                   | `element[attribute="value"]`        | Matches exact value                         |
| Starts with                   | `element[attribute^="value"]`       | Value starts with given string              |
| Ends with                     | `element[attribute$="value"]`       | Value ends with given string                |
| Contains substring            | `element[attribute*="value"]`       | Value contains the substring                |

#### 🧪 Example

```html
<input type="text" placeholder="Text input">
<input type="password" placeholder="Password input">
<a href="https://example.com">Secure Link</a>
<a href="http://example.com">Normal Link</a>
```

```css
input[type="text"] {
  border: 2px solid blue;
}
a[href^="https"] {
  color: green;
}
```

---

### 2. 🔗 Combinator Selectors

Combinators define relationships between elements and allow you to style elements based on their position in the DOM.

#### 🔹 Types of Combinators

| Combinator        | Syntax        | Description                                      |
|-------------------|---------------|--------------------------------------------------|
| Descendant        | `A B`         | Selects all B inside A (any depth)              |
| Child             | `A > B`       | Selects B that is a direct child of A           |
| Adjacent sibling  | `A + B`       | Selects B immediately after A                   |
| General sibling   | `A ~ B`       | Selects all B siblings after A                  |

#### 🧪 Examples

```html
<!-- Descendant -->
<div>
  <p>Styled</p>
</div>
<p>Not styled</p>

<!-- Child -->
<div>
  <p>Direct child</p>
  <section><p>Nested child</p></section>
</div>

<!-- Adjacent -->
<h2>Heading</h2>
<p>Styled paragraph</p>
<p>Not styled</p>

<!-- General Sibling -->
<h2>Heading</h2>
<p>Sibling 1</p>
<p>Sibling 2</p>
<div><p>Not a sibling</p></div>
```

```css
div p {
  color: blue; /* Descendant */
}
div > p {
  color: green; /* Child */
}
h2 + p {
  color: red; /* Adjacent */
}
h2 ~ p {
  color: purple; /* General sibling */
}
```

---

## 🧠 Quiz Recap

1. **What does `a[target="_blank"]` select?**  
   → All `<a>` elements with `target="_blank"`.

2. **Which combinator selects direct children?**  
   → `div > p`

---

## 🛠️ Practice Task

Create an HTML form with:

- A text input → styled with gray border
- An email input → styled with blue border
- A submit button → green background, white text

Then, practice all four combinator selectors using nested elements.

---

## 📚 References

- [MDN Web Docs – CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [W3Schools – CSS Tutorial](https://www.w3schools.com/css/)
- [CSS-Tricks](https://css-tricks.com/)

---

## ✅ Tips for Mastery

- Use browser DevTools to inspect and test selectors live
- Try combining attribute and combinator selectors for advanced targeting
- Practice writing selectors without relying on classes or IDs

---
