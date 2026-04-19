## Hotel Performance Analysis based on Agoda Reviews

### About the dataset

The dataset contains 74 reviews.

Each review has the following fields: id, createdAt, language, comments.

![Image1](/images/reviews_per_year.png) ![Image2](/images/reviews_per_month.png)

_The reviews from Airbnb website fluctuates after 2022. This could be an indication that airbnb may not be the recent website customers visit in the past three years.<br> It is also revealed that most posters tend to post their reviews around the summer months(June and July), which could be an indication that those are the peak months for tourists. On the other hand, the non-holiday seasons like January and October are the weakest months for tourists._

![Image3](/images/problematic_comments.png)

![Image3](/images/problematic_comments.png)

_The majority of the comments do not have underlying problems, but there are still a significant number of comments that indicate potential issues. This suggests that while many customers may be satisfied, there is a notable portion of feedback that points to areas for improvement. There are 10 have underlying problems._

### Visualizing the Comments

Here are the most common unigrams, bigrams, and trigrams found in the reviews. These n-grams can provide insights into common themes and issues mentioned by customers. For instance, if we see frequent bigrams like 'room service' or 'customer support', it may indicate areas that customers frequently discuss, whether positively or negatively. Analyzing these n-grams can help identify key areas of strength and opportunities for improvement in the hotel services._

![Image1](/images/top_15_unigrams_—_full_corpus.png) ![Image2](/images/top_15_bigrams_—_full_corpus.png) ![Image3](./images/top_15_trigrams_—_full_corpus.png)

### Bigram of Non-Problematic Reviews vs. Problematic Reviews

Here are the most common unigrams, bigrams, and trigrams found in the two types of reviews

![Image1](/images/top_bigrams_by_problem.png)

#### Word Cloud Visualization

GENERAL CORPUS

![Image3](/images/wordcloud_full_corpus.png)

##Good vs Bad Reviews

![Image1](/images/wordcloud_good_reviews.png) ![Image2](/images/wordcloud_bad_reviews.png)

Here are all the comments that have underlying problems:

  - We had a very nice stay. The place is a bit far from town proper and hard to hail a taxi or tricycle going to town proper

  - Friendly staff. Greets us every time they see us. Very helpful too in giving directions and places where we can get food.<br/>The place is also sparkling clean. The towels provided and new and clean too. Amenities are adequate and they are willing to replenish them and change the towels if you stay more than one nights.<br/>The location is very near Magsaysay and accessible thru tricycles.<br/>Just a few things to improve on:<br/>•I wish that this room also has a water heater (for drinking) like the other rooms<br/>•I noticed the lack of security cameras in the hallways, not sure if the lobby has<br/>•There is no cafeteria where guests can order coffee or breakfast although the laundry service at the ground floor has a vendo for coffee<br/>•The wifi reception can be improved. The signal fluctuates maybe bc our room is at the very far end of the building<br/>These are very minor flaws but this place is ideal for a quick stay. It’s value for money, clean and accessible.

  - Location was great. But since the place is new, not all tricycle drivers knew the place

  - nice clean place. bed is a bit small and only 2 pillows. no table, glasses, plates etc. but the location is excellent, kinalas country! very near center, almost every place is a trike away. thanks!

  - The room is very clean and there is a lot of space, but I could not sleep properly because the windows are so thin, so I heard all the noise in the streets of the motors of the vehicles or the peoples outdoor. And also there is no possibility to stay in the dark when it's the day. So the windows let enter all the light. I could not rest and was always woke up by the noise in the street, so I could not stay there anymore. The price is good and the location is near the main avenue and not far from the malls, but what's the point of staying in a hotel if I can't sleep properly in the bed. And also the foam was so thin and little. So I really didn't sleep well unfortunately.

  - The room is very clean, the staffs are very friendly and accommodating. The only issue that I encountered was the wifi it is very fast and stable, but the hassle of getting the login credentials at the reception every 24 hours because it expires. I also worked when I stayed there, and that's the only hassle I experienced staying there. But so far, I will still recommend this place to my friends looking for a clean place to stay in Naga City. Cheers! 

  - Overall, really good. Only thing though is the shower. It's either too hot or too cold. there's no in between and sometimes difficult to move the know especially for someone short.

  - I requested upon check in to give us a room sa lower floors kasi puro seniors yung kasama ko tapos binigay smin 4th flr na. Pagod na pagod tuloy sila. Then, When we checked in hindi kami binigyan ng wifi pass. The night after we checked in pumunta pa ung attendant sa room to get the balance payment. Night before checkout na tska ko lang nakita kasi nagbigay sila sa new guest tapos sabi ko may wifi pala? They should know na upon check in dapat bibigay na yon. Yung kumot namin may butas pa sana naman chineck un pero cleanliness okay naman, appliances all working naman. Still giving 4 stars host is responsive and clean naman.

  - Room was spacious and clean. Big cabinets and bed was really great. Fast food chains and restaurants are about 5 mins drive from the area. The only downside was sound of motorcycles outside can be heard inside the room which slightly disturbed our sleep.

  - The host was completely unresponsive, and it caused a lot of confusion when I arrived. My check-in time was 2 PM, but the front desk staff didn’t seem to know what room I was supposed to have. The Airbnb listing didn’t include enough details about the room, and since the host wasn’t replying, I couldn’t provide much information.<br/>When I showed proof of payment and my Airbnb confirmation email with my full name, the front desk woman still wasn’t willing to help. I even asked for the host’s contact number, and only then did she check her record book and confirm that I was listed. When I asked what room I should go to, she kept giving vague and sarcastic responses instead of just telling me directly. It was very frustrating and unprofessional.<br/>Also, around 3-5 AM, another front desk woman was sleeping on the couch, leaving the area unattended. There was no security guard on duty, and it felt unsafe.<br/>I hope future guests won’t experience the same poor service and lack of communication.
