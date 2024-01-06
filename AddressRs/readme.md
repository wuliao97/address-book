# Address-Book with Rust

---

### Env

- [rustc](https://doc.rust-lang.org/rustc/index.html) 1.74.0 (79e9716c9 2023-11-13)
- [cargo](https://doc.rust-lang.org/stable/cargo/) 1.74.0 (ecb9851af 2023-10-18)
- Editor - [RustRover](https://www.jetbrains.com/ja-jp/rust/) by [JetBrains](https://www.jetbrains.com/ja-jp/)

---

### Requirements
```toml
[dependencies]
anyhow = "1.0.79"
sqlx = { version = "0.7.3", features = ["sqlite", "runtime-async-std-native-tls"]}
tokio = { version = "1.35.1", features = ["full"] }
```

---

## Improvement points

- Add a Indexing in DB. I meant optimization Database
- Make more the Flexible Code
- Use another DB (for afraid to become big data
- I gotta know Why need `Option<String>` at ./src/model.rs/L3