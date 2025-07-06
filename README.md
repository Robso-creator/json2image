# json2image

main goal for this repository is create an API capable of generating images using HTML and CSS through a POST on an endpoint

# Request example

```json
{
	"h": 250,
	"w": 250,
	"background": "black",
	"elements": [
		{
			"type": "text", 
			"position": [0, 0], 
			"font": "Nunito", 
			"color": "white", 
			"size": 20,
			"value": "Aloha"
		},
		{
			"type": "text", 
			"position": "center", 
			"font": "Nunito", 
			"color": "white", 
			"size": 20,
			"value": "Aloha"
		},
		{
			"type": "text", 
			"position": "bottom-center", 
			"font": "Nunito", 
			"color": "white", 
			"size": 20,
			"value": "Aloha"
		}
	]
}
```

When building this app I said to myself that the first company image to show up on my timeline I should be capable of
recreating via Json2Image. So I would be able to say that it can be used on real scenarios.

This Databricks post was the first one to show up:

![databricks_img.png](databricks_img.png)