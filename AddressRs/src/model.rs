#[derive(Debug)]
pub struct AddrModel {
    pub name: Option<String>,
    pub phone_number: String,
    pub address_line: String,
    pub city: String,
    pub region: String,
    pub country: String,
    pub post_code: String
}

impl AddrModel {
    pub fn new<T: ToString>(
        name: T,
        phone_number: T,
        address_line: T,
        city: T,
        region: T,
        country: T,
        post_code: T
    ) -> Self {

        Self {
            name: Some(name.to_string()),
            phone_number: phone_number.to_string(),
            address_line: address_line.to_string(),
            city: city.to_string(),
            region: region.to_string(),
            country: country.to_string(),
            post_code: post_code.to_string(),
        }
    }
}
