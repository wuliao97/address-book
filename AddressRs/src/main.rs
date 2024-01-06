mod util;
mod sql;
mod model;

use crate::sql::{
    get_conn, get_one, insert_or_update
};

use crate::model::AddrModel;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let conn = get_conn().await?;
    let name = "Ennui";
    let addr = AddrModel::new(
        name,
        "8170-0000-111",
        "0000",
        "Chiyodaku",
        "Tokyo-to",
        "Japan",
        "1000 000",
    );
    insert_or_update(&conn, addr)
        .await;

    let result = get_one(&conn, name.to_string())
        .await?;
    dbg!(result);

    Ok(())
}
