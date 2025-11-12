# 🎯 CSS Session 3 – CSS Selectors & Properties (Lecture 11)

This README is a complete reference guide for **Lecture 11: CSS Selectors & Properties – I** from Web Development-I . It explains how selectors target HTML elements and how properties define their styling.

---

## 📘 What are CSS Selectors & Properties?

- **Selectors**: Patterns used to target HTML elements on a webpage.  
  👉 They tell the browser **where** to apply styles.

- **Properties**: Define **what** styling to apply (e.g., color, font-size, margin).  
  👉 They control the **appearance** of the selected elements.

> Without selectors, CSS wouldn’t know which elements to style.

---

## 🧩 Types of CSS Selectors

1. **Basic Selectors**
   - Type Selectors (by tag name)
   - Class Selectors (by class attribute)
   - ID Selectors (by unique id)

2. **Attribute Selectors** *(covered in later sessions)*

3. **Combinator Selectors** *(covered in later sessions)*

---

## 🔹 Basic Selectors

### 1️⃣ Type Selector

- Targets all elements of a specific tag (e.g., all `<p>` or all `<h1>`).
- **Syntax:**

  ```css
  tagname {
    property: value;
  }
  ```

- **Example:**

  ```html
  <style>
    p {
      color: blue;
    }
  </style>
  <p>Hello, world!</p>
  <p>This is CSS type selector.</p>
  ```

- ✅ Both `<p>` elements will be blue.

---

### 2️⃣ Class Selector

- Targets elements with a specific `class` attribute.
- Can be reused across multiple elements.
- **Syntax:**

  ```css
  .classname {
    property: value;
  }
  ```

- **Example:**

  ```html
  <style>
    .box {
      color: green;
    }
  </style>
  <p class="box">This is styled with a class.</p>
  <p>This is not styled.</p>
  ```

- ✅ Only the `<p>` with `class="box"` is green.

---

### 3️⃣ ID Selector

- Targets a single unique element with an `id` attribute.
- IDs must be unique per page.
- **Syntax:**

  ```css
  #idname {
    property: value;
  }
  ```

- **Example:**

  ```html
  <style>
    #header {
      color: red;
    }
  </style>
  <h1 id="header">This is styled with an ID.</h1>
  <h1>This is not styled.</h1>
  ```

- ✅ Only the `<h1>` with `id="header"` is red.

---

## 🎯 CSS Sniper Analogy

Think of CSS selectors like a sniper choosing targets:

- **Type Selector (`p`)** → All soldiers wearing the same uniform (all `<p>` tags).
- **Class Selector (`.hero`)** → A special squad with unique badges (all elements with class `hero`).
- **ID Selector (`#leader`)** → One specific soldier with a unique call sign (the element with ID `leader`).

---
<!--
📘 CSS Properties Cheat Sheet
This section summarizes common CSS properties with examples.
You can paste this into your README or HTML documentation.
-->
```html
<style>
  /* Text styling */
  .text-example {
    color: #333; /* Sets text color */
    font-size: 18px; /* Sets font size */
    font-family: 'Segoe UI', sans-serif; /* Sets font style */
    font-weight: bold; /* Makes text bold */
    text-align: center; /* Centers the text */
    text-decoration: underline; /* Underlines the text */
  }

  /* Box model */
  .box-example {
    margin: 20px; /* Space outside the element */
    padding: 10px; /* Space inside the element */
    border: 2px solid #000; /* Adds a border */
    width: 300px; /* Sets width */
    height: 150px; /* Sets height */
  }

  /* Layout and effects */
  .layout-example {
    display: flex; /* Enables flex layout */
    position: relative; /* Enables positioning */
    top: 10px; /* Moves element down */
    left: 10px; /* Moves element right */
    z-index: 5; /* Stacking order */
    overflow: hidden; /* Hides overflow content */
    opacity: 0.8; /* Transparency */
    visibility: visible; /* Element is visible */
    box-shadow: 2px 2px 8px rgba(0,0,0,0.2); /* Adds shadow */
    transition: all 0.3s ease; /* Smooth animation */
    transform: scale(1.1); /* Scales the element */
    cursor: pointer; /* Changes mouse cursor */
  }
</style>

<div class="text-example">Text Styling Example</div>
<div class="box-example">Box Model Example</div>
<div class="layout-example">Layout & Effects Example</div>
```
