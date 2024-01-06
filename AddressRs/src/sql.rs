use anyhow::Result;
use sqlx::Executor;
use crate::model::AddrModel;

pub async fn get_conn() -> Result<sqlx::SqlitePool> {
    let url = "./db/address.db";
    Ok(sqlx::sqlite::SqlitePool::connect(url).await?)
}


pub async fn insert_or_update(pool: &sqlx::SqlitePool, model: AddrModel) -> sqlx::sqlite::SqliteQueryResult {
    sqlx::query!(r#"INSERT INTO address values (?, ?, ?, ?, ?, ?, ?)
                 ON CONFLICT (name) DO UPDATE SET
                 phone_number = ?, address_line = ?, city = ?, region = ?, country = ?, post_code = ?"#,
                 model.name, model.phone_number, model.address_line, model.city, model.region, model.country, model.post_code,
                 model.phone_number, model.address_line, model.city, model.region, model.country, model.post_code
                 )
        .execute(pool)
        .await
        .unwrap()
}

pub async fn get_one(pool: &sqlx::SqlitePool, key: String) -> Result<AddrModel> {
    let result = sqlx::query_as!(AddrModel, "SELECT * FROM address WHERE name = ?", key)
        .fetch_one(pool)
        .await?;
    Ok(result)
}