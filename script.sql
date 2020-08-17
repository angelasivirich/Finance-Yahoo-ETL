CREATE TABLE "USDxCAD_ExchangeRate" (
    "Date" date   NOT NULL,
    "USDXCAD" float   NOT NULL
);

CREATE TABLE "COVID_Cases" (
    "Date" date   NOT NULL,
    "daily_new_cases" int   NOT NULL,
    "total_cases" int   NOT NULL,
    CONSTRAINT "pk_COVID_Cases" PRIMARY KEY (
        "Date"
     )
);

CREATE TABLE "Stock_Dataframe" (
    "Date" date   NOT NULL,
    "Air_Canada_open" float   NOT NULL,
    "Air_Canada_close" float   NOT NULL,
    "Air_Canada_pert_change" float   NOT NULL,
    "Oil_open" float   NOT NULL,
    "Oil_close" float   NOT NULL,
    "Oil_pert_change" float   NOT NULL,
    "Gold_open" float   NOT NULL,
    "Gold_close" float   NOT NULL,
    "Gold_pert_change" float   NOT NULL,
    "Pton_open" float   NOT NULL,
    "Pton_close" float   NOT NULL,
    "Pton_pert_change" float   NOT NULL,
    "Loblaws_open" float   NOT NULL,
    "Loblaws_close" float   NOT NULL,
    "Loblaw_pert_change" float   NOT NULL,
    "Amazon_open" float   NOT NULL,
    "Amazon_close" float   NOT NULL,
    "Amazon_pert_change" float   NOT NULL,
    "netflix_open" float   NOT NULL,
    "netflix_close" float   NOT NULL,
    "netflix_pert_change" float   NOT NULL,
    "uber_open" float   NOT NULL,
    "uber_close" float   NOT NULL,
    "uber_pert_change" float   NOT NULL
);

