DROP TABLE samples;

CREATE TABLE samples AS 
SELECT 
   P.NAME AS name,
   P.DESCRIPTION AS description,
   P.MANUFACTURER AS manufacturer,
    MAX(C1.NAME) AS cat_1, 
    MAX(C2.NAME) AS cat_2, 
    MAX(C3.NAME) AS cat_3, 
    MAX(C4.NAME) AS cat_4, 
    MAX(C5.NAME) AS cat_5, 
    MAX(C6.NAME) AS cat_6, 
    MAX(C7.NAME) AS cat_7,
    MAX(C8.NAME) AS cat_8
FROM 
    PRODUCTS P
INNER JOIN 
    PRODUCTCATEGORY PC 
    ON PC.PRODUCTID = P.ID
INNER JOIN 
    CATEGORIES C1 
    ON C1.ID = PC.CATEGORYID
LEFT OUTER JOIN 
    SUBCATEGORIES SC1 
    ON C1.ID = SC1.SUBCATEGORYID
LEFT OUTER JOIN 
    CATEGORIES C2 
	ON C2.ID = SC1.CATEGORYID
	AND EXISTS (
		SELECT 
			1
		FROM 
			PRODUCTCATEGORY PC1
			WHERE PC1.PRODUCTID = P.ID AND C2.ID = PC1.CATEGORYID)
LEFT OUTER JOIN 
    SUBCATEGORIES SC2 
    ON C2.ID = SC2.SUBCATEGORYID
LEFT OUTER JOIN 
    CATEGORIES C3 
    ON C3.ID = SC2.CATEGORYID
	AND EXISTS (
		SELECT 
			1
		FROM 
			PRODUCTCATEGORY PC2
			WHERE PC2.PRODUCTID = P.ID AND C3.ID = PC2.CATEGORYID)
LEFT OUTER JOIN 
    SUBCATEGORIES SC3 
    ON C3.ID = SC3.SUBCATEGORYID
LEFT OUTER JOIN 
    CATEGORIES C4 
    ON C4.ID = SC3.CATEGORYID
	AND EXISTS (
		SELECT 
			1
		FROM 
			PRODUCTCATEGORY PC3
			WHERE PC3.PRODUCTID = P.ID AND C4.ID = PC3.CATEGORYID)
LEFT OUTER JOIN 
    SUBCATEGORIES SC4 
    ON C4.ID = SC4.SUBCATEGORYID
LEFT OUTER JOIN 
    CATEGORIES C5 
    ON C5.ID = SC4.CATEGORYID
	AND EXISTS (
		SELECT 
			1
		FROM 
			PRODUCTCATEGORY PC4
			WHERE PC4.PRODUCTID = P.ID AND C5.ID = PC4.CATEGORYID)
LEFT OUTER JOIN 
    SUBCATEGORIES SC5 
    ON C5.ID = SC5.SUBCATEGORYID
LEFT OUTER JOIN 
    CATEGORIES C6 
    ON C6.ID = SC5.CATEGORYID
	AND EXISTS (
		SELECT 
			1
		FROM 
			PRODUCTCATEGORY PC5
			WHERE PC5.PRODUCTID = P.ID AND C6.ID = PC5.CATEGORYID)
LEFT OUTER JOIN 
    SUBCATEGORIES SC6 
    ON C6.ID = SC6.SUBCATEGORYID
LEFT OUTER JOIN 
    CATEGORIES C7 
    ON C7.ID = SC6.CATEGORYID
	AND EXISTS (
		SELECT 
			1
		FROM 
			PRODUCTCATEGORY PC6
			WHERE PC6.PRODUCTID = P.ID AND C7.ID = PC6.CATEGORYID)
LEFT OUTER JOIN 
    SUBCATEGORIES SC7
    ON C7.ID = SC7.SUBCATEGORYID
LEFT OUTER JOIN 
    CATEGORIES C8 
    ON C8.ID = SC7.CATEGORYID
	AND EXISTS (
		SELECT 
			1
		FROM 
			PRODUCTCATEGORY PC7
			WHERE PC7.PRODUCTID = P.ID AND C8.ID = PC7.CATEGORYID)
WHERE 
    NOT EXISTS (
		SELECT
            1 
		FROM 
            SUBCATEGORIES SC 
		WHERE 
            SC.CATEGORYID = C1.ID)
GROUP BY 
    P.ID,
    P.NAME	
ORDER BY 
    P.ID;