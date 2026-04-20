## Hotel Performance Analysis based on Airbnb Reviews

A data-driven exploration of customer sentiment and experience using Airbnb hotel reviews. This project combines natural language processing (NLP) techniques with machine learning to uncover what guests truly think—highlighting strengths, exposing weaknesses, and translating insights into actionable business recommendations.

This project automatically saves a markdown file detailing the entire review corpus and summary of its insights. 



## THIS IS AN EXAMPLE OF THE MARKDOWN FILE GENERATED

---

### About the dataset

The dataset contains 74 reviews.

Each review has the following fields: id, createdAt, language, comments.

![Image1](/images/reviews_per_year.png) ![Image2](/images/reviews_per_month.png)

_The reviews from Airbnb website fluctuates after 2022. This could be an indication that airbnb may not be the recent website customers visit in the past three years.<br> It is also revealed that most posters tend to post their reviews around the summer months(June and July), which could be an indication that those are the peak months for tourists. On the other hand, the non-holiday seasons like January and October are the weakest months for tourists._

![Image3](/images/problematic_comments.png)

_The majority of the comments do not have underlying problems, but there are still a significant number of comments that indicate potential issues. This suggests that while many customers may be satisfied, there is a notable portion of feedback that points to areas for improvement. There are 10 have underlying problems._

### Visualizing the Comments

Here are the most common unigrams, bigrams, and trigrams found in the reviews. These n-grams can provide insights into common themes and issues mentioned by customers. For instance, if we see frequent bigrams like 'room service' or 'customer support', it may indicate areas that customers frequently discuss, whether positively or negatively. Analyzing these n-grams can help identify key areas of strength and opportunities for improvement in the hotel services._

![Image1](/images/top_15_unigrams_—_full_corpus.png) ![Image2](/images/top_15_bigrams_—_full_corpus.png) ![Image3](/images/top_15_trigrams_—_full_corpus.png)

### TF-IDF of Non-Problematic Reviews vs. Problematic Reviews
![Image5](/images/tfidf_top_terms_by_problem.png)

### Bigram of Non-Problematic Reviews vs. Problematic Reviews

Here are the most common bigrams in the entire review section

![Image1](/images/top_bigrams_by_problem.png)



### Word Cloud Visualization

### GENERAL CORPUS

![Image3](/images/wordcloud_full_corpus.png)

### Good vs Bad Reviews

![Image1](/images/wordcloud_good_reviews.png) ![Image2](/images/wordcloud_bad_reviews.png)

Here are some comments that have underlying problems:

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


<br/>
<br/>
<br/>


## Summary of Problems(16)


![Image4](/images/elbow_silhouette.png)

Using K-Means clustering, the problems were clustered into 16 general problems:

**1. Remote Location and Transport Issues (2)**

    - Hotel located far from town proper
    - Difficulty in hailing taxis or tricycles to town proper
**2. Front Desk Service Issues (3)**

    - Lack of front desk staff knowledge about room assignments
    - Rude and unhelpful behavior of front desk staff
    - Front desk being unattended during nighttime
**3. Room Amenities and Security Issues (15)**

    - Insufficient room amenities (pillows, table, glasses, plates)
    - Noise disturbances affecting sleep (street noise, motorcycle noise)
    - Security concerns (lack of security cameras, no security guard on duty)
    - Room comfort and usability issues (thin mattress, difficult shower knob, problematic for shorter guests)
    - Connectivity inconvenience (wifi credentials expiring every 24 hours)
    - Poor host responsiveness and communication (unresponsive host, vague and sarcastic responses)
**4. Hotel Experience Issues (2)**

    - Poor sound insulation causing noise disturbances
    - Poor communication between staff and guests
**5. WiFi Access Issues (1)**

    - WiFi password not provided at check-in
**6. Safety Issues (1)**

    - Safety concerns
**7. Room Cleanliness and Maintenance (1)**

    - Damaged bedding or linens
**8. Local Transportation Issues (1)**

    - Driver unfamiliarity with hotel location
**9. Bathroom Comfort Issues (1)**

    - Difficulty adjusting shower temperature
**10. Payment Process Issues (1)**

    - Payment collected at night before checkout
**11. Room Comfort Issues (1)**

    - Bed size smaller than expected
**12. Poor WiFi Connectivity (1)**

    - Weak WiFi signal strength
    - Fluctuating or unstable WiFi connectivity
**13. Lack of Drinking Water Facilities (1)**

    - No water heater available for drinking water
**14. Room Lighting Issues (1)**

    - excessive natural light entering the room causing discomfort
**15. Lack of Onsite Food Amenities (1)**

    - No cafeteria for coffee
    - No breakfast facilities available
**16. Room Location Issues (1)**

    - Assigned upper floor instead of requested lower floor
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


---
# Discussion of Problems
---
## Problem #1: Location and Transportation (2)

The problems relate to the hotel's inconvenient location far from the town center and difficulties guests face in securing transportation to reach town amenities.

### Keywords
location, distance, transportation, accessibility, taxi, tricycle

### Subproblems
- Hotel located far from town proper
- Difficulty in hailing taxis or tricycles to town proper

### Recommendations
- Provide shuttle services or arrange reliable transport options for guests to and from town.
- Offer clear guidance or assistance with booking local transportation.
- Improve communication about the hotel's location and transport options before booking.

---

## Problem #2: Front Desk Service Issues (3)

These problems all relate to negative experiences with front desk service, including staff knowledge, attitude, and availability, indicating a common issue with front desk operations and customer service.

### Keywords
front desk, staff knowledge, rude service, unattended desk, night service

### Subproblems
- Lack of front desk staff knowledge about room assignments
- Rude and unhelpful behavior of front desk staff
- Front desk being unattended during nighttime

### Recommendations
- Provide comprehensive training to front desk staff to ensure accurate and up-to-date knowledge of room assignments.
- Implement customer service training and monitor staff interactions to improve politeness and helpfulness.
- Ensure 24/7 front desk coverage or provide a reliable alternative for guest assistance during nighttime.

---

## Problem #3: Room Amenities and Security Issues (15)

This cluster groups together problems related to inadequate room amenities, noise disturbances, and security concerns, reflecting issues that directly affect guest comfort and safety during their stay.

### Keywords
amenities, security, noise, comfort, facilities

### Subproblems
- Insufficient room amenities (pillows, table, glasses, plates)
- Noise disturbances affecting sleep (street noise, motorcycle noise)
- Security concerns (lack of security cameras, no security guard on duty)
- Room comfort and usability issues (thin mattress, difficult shower knob, problematic for shorter guests)
- Connectivity inconvenience (wifi credentials expiring every 24 hours)
- Poor host responsiveness and communication (unresponsive host, vague and sarcastic responses)

### Recommendations
- Amenities: Ensure rooms are equipped with essential items such as adequate pillows, tables, glasses, and plates to enhance guest comfort.
- Noise: Implement soundproofing measures or provide noise-cancelling options such as earplugs to minimize disturbances from external noises.
- Security: Improve guest safety by installing security cameras in hallways and ensuring security personnel are present on duty.
- Room Comfort: Upgrade mattresses to better quality foam and address shower usability concerns; consider adaptations for guests of varying heights.
- Connectivity: Provide longer-lasting or more convenient wifi access credentials to avoid frequent re-authentication.
- Host Communication: Train staff to respond promptly and politely to guest inquiries to improve overall satisfaction.

---

## Problem #4: Hotel Experience Issues (2)

The problems relate to different aspects of guest dissatisfaction during their stay, including both physical comfort and service quality, which impact the overall hotel experience.

### Keywords
sound insulation, communication, guest satisfaction, hotel experience

### Subproblems
- Poor sound insulation causing noise disturbances
- Poor communication between staff and guests

### Recommendations
- For poor sound insulation: Conduct an audit of room acoustics and invest in soundproofing improvements such as better windows, doors, or insulation materials.
- For poor communication: Enhance staff training on guest interaction, implement clear communication protocols, and provide multiple channels for guests to reach staff easily.

---

## Problem #5: WiFi Access Issues (1)

All problems in this cluster relate to difficulties guests face in accessing or using the hotel's WiFi services, primarily focusing on missing or unavailable WiFi passwords.

### Keywords
WiFi, password, access, check-in

### Subproblems
- WiFi password not provided at check-in

### Recommendations
- Ensure WiFi passwords are readily available and communicated clearly during check-in.
- Train front desk staff to proactively provide WiFi access details.
- Consider displaying WiFi credentials in rooms or common areas to reduce guest inconvenience.

---

## Problem #6: Safety Issues (1)

This cluster contains problems related to guests' concerns about their personal safety during their stay at the hotel. These issues are centered around the hotel's ability to provide a secure environment for its guests.

### Keywords
safety, security, personal safety, guest protection

### Subproblems
- Safety concerns

### Recommendations
- Enhance security measures such as installing surveillance cameras and increasing security personnel presence.
- Provide clear information about safety protocols to guests.
- Conduct regular safety audits to identify and mitigate risks.

---

## Problem #7: Room Cleanliness and Maintenance (1)

This cluster focuses on issues related to the physical condition and cleanliness of the hotel room, indicating a problem with room upkeep.

### Keywords
cleanliness, maintenance, room condition, damaged items, hygiene

### Subproblems
- Damaged bedding or linens

### Recommendations
- Implement more thorough room inspections before guest check-in to identify and replace damaged items like blankets.
- Establish a routine maintenance and housekeeping checklist to ensure all linens and room materials meet quality standards prior to guest arrival.

---

## Problem #8: Local Transportation Issues (1)

This cluster focuses on difficulties related to local transport, particularly problems with drivers not being familiar with the hotel location or destination.

### Keywords
tricycle drivers, driver knowledge, local transport, directions

### Subproblems
- Driver unfamiliarity with hotel location

### Recommendations
- Coordinate with local transport providers to ensure drivers assigned to hotel guests know the location well.
- Provide guests with detailed address information and landmarks to share with drivers.
- Implement a shuttle service or arrange trusted transportation partners familiar with the hotel.

---

## Problem #9: Bathroom Comfort Issues (1)

This cluster groups problems related to discomfort or inconvenience specifically experienced in the bathroom area, particularly focusing on the usability and functionality of the shower.

### Keywords
shower, temperature, adjustment, bathroom, comfort

### Subproblems
- Difficulty adjusting shower temperature

### Recommendations
- Perform regular maintenance and inspection of shower mixing valves to ensure they respond to temperature adjustments smoothly.
- Consider upgrading to thermostatic shower valves for better temperature control and safety.
- Provide clear instructions for guests on how to adjust the shower temperature if the system is not intuitive.

---

## Problem #10: Payment Process Issues (1)

The problem relates to unexpected or inconvenient payment collection timing, which can cause customer discomfort or confusion.

### Keywords
payment, balance, checkout, timing, attendant

### Subproblems
- Payment collected at night before checkout

### Recommendations
- Establish clear payment policies communicated at check-in.
- Standardize payment collection timing to daytime hours.
- Train staff to avoid collecting payments during inconvenient times.
- Provide guests with payment schedule upon arrival to reduce surprises.

---

## Problem #11: Room Comfort Issues (1)

This cluster groups issues related to the comfort of the room, specifically focusing on the bed size and sleeping arrangements.

### Keywords
bed, small, room comfort

### Subproblems
- Bed size smaller than expected

### Recommendations
- Provide clear information about bed sizes in room descriptions to set guest expectations.
- Offer room options with larger beds for guests needing extra comfort.
- Consider upgrading or replacing smaller beds if feasible to enhance guest satisfaction.

---

## Problem #12: Poor WiFi Connectivity (1)

This cluster revolves around issues related to unstable and weak WiFi, which impacts guest experience by limiting internet access and reliability.

### Keywords
WiFi, connectivity, signal, reception, internet, unstable

### Subproblems
- Weak WiFi signal strength
- Fluctuating or unstable WiFi connectivity

### Recommendations
- Conduct a thorough assessment of the WiFi infrastructure to identify dead zones and areas with poor signal strength.
- Upgrade WiFi access points to models with better range and stability, ensuring even coverage throughout the property.
- Regularly maintain and monitor network equipment to prevent fluctuations and outages.
- Provide guest support and clear instructions on connecting to reliable WiFi networks.

---

## Problem #13: Lack of Drinking Water Facilities (1)

This cluster focuses on issues related to the availability and convenience of drinking water in the hotel, highlighting a lack of water heating options.

### Keywords
no water heater, drinking water, water facilities

### Subproblems
- No water heater available for drinking water

### Recommendations
- Install water heaters or provide hot water dispensers in rooms or common areas to facilitate access to hot drinking water.

---

## Problem #14: Room Lighting Issues (1)

This cluster highlights guest dissatisfaction related to the room's lighting conditions, specifically concerns about excessive natural light entering the room.

### Keywords
room, lighting, too much light, brightness, natural light

### Subproblems
- excessive natural light entering the room causing discomfort

### Recommendations
- Install adjustable blackout curtains or blinds to allow guests control over the amount of natural light.
- Consider room orientation and window treatments during room design or renovation to minimize excessive light entry.

---

## Problem #15: Lack of Onsite Food Amenities (1)

This cluster centers around the absence of dining options within the hotel, specifically the lack of a cafeteria or facilities for coffee and breakfast, impacting guest convenience and satisfaction.

### Keywords
no cafeteria, no breakfast options, no onsite dining, lack of coffee service

### Subproblems
- No cafeteria for coffee
- No breakfast facilities available

### Recommendations
- Consider introducing a cafeteria or coffee bar to provide convenient onsite breakfast and coffee options.
- Partner with local cafes or implement room service breakfast to improve guest dining experience.
- Promote nearby food options clearly in the hotel information to mitigate guest inconvenience.

---

## Problem #16: Room Location Issues (1)

This cluster includes problems related to guests not receiving their requested room floor location, indicating a mismatch between the booking preferences and actual room assignment.

### Keywords
room location, floor assignment, requested floor, room allocation

### Subproblems
- Assigned upper floor instead of requested lower floor

### Recommendations
- Improve the room assignment system to prioritize guest floor preferences during check-in.
- Train front desk staff to verify room requests and confirm floor allocations with guests.
- Update the booking system to flag floor preferences clearly and communicate them to housekeeping and allocation teams.

---




<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


---
# Recommendations
---

**1: Remote Location and Transport Issues**

  - Provide **shuttle services** or arrange reliable transport options for guests to and from town.
  - Offer **clear guidance** or assistance with booking local transportation.
  - Improve **communication about the hotel's location** and transport options before booking.

**2: Front Desk Service Issues**

  - Provide **comprehensive training** to front desk staff to ensure accurate and up-to-date knowledge of room assignments.
  - Implement **customer service training** and **monitor staff interactions** to improve politeness and helpfulness.
  - Ensure **24/7 front desk coverage** or provide a reliable alternative for **guest assistance during nighttime**.

**3: Room Amenities and Security Issues**

  - Amenities: Ensure rooms are equipped with essential items such as **adequate pillows, tables, glasses, and plates** to enhance guest comfort.
  - Noise: Implement **soundproofing measures** such as earplugs to minimize disturbances from external noises.
  - Security: Improve guest safety by installing **security cameras in hallways** and ensuring security personnel are present on duty.
  - Room Comfort: **Upgrade mattresses** to better quality foam and **address shower usability concerns**; consider adaptations for guests of varying heights.
  - Connectivity: Provide longer-lasting or more convenient **wifi access credentials to avoid frequent re-authentication**.
**4: Hotel Experience Issues**

  - For poor sound insulation: Conduct an audit of room acoustics and invest in soundproofing improvements such as better windows, doors, or insulation materials.
  - For poor communication: Enhance staff training on guest interaction, implement clear communication protocols, and provide multiple channels for guests to reach staff easily.

**5: WiFi Access Issues**

  - Ensure **WiFi passwords are readily available** and communicated clearly during check-in.
  - Train front desk staff to proactively provide WiFi access details.
  - Consider **displaying WiFi credentials in rooms** or common areas to reduce guest inconvenience.

**6: Safety Issues**

  - Enhance security measures such as installing **surveillance cameras** and increasing **security personnel** presence.
  - Provide clear information about safety protocols to guests.
  - Conduct regular safety audits to identify and mitigate risks.

**7: Room Cleanliness and Maintenance**

  - Implement more thorough **room inspections before guest check-in** to identify and **replace damaged items** like blankets.
  - Establish a **routine maintenance** and **housekeeping checklist** to ensure all linens and room materials meet quality standards prior to guest arrival.

**8: Local Transportation Issues**

  - Leverage **social media** to inform guests of the landmark and map.
  - Provide guests with detailed address information and **landmarks** to share with drivers.
  
**9: Bathroom Comfort Issues**

  - Perform regular **maintenance and inspection of shower mixing valves** to ensure they respond to **temperature adjustments** smoothly.
  - Consider upgrading to **thermostatic shower valves** for better temperature control and safety.
  - Provide clear instructions for guests on how to adjust the shower temperature if the system is not intuitive.

**10: Payment Process Issues**

  - Establish **clear payment policies** communicated at check-in.
  - **Standardize payment collection timing** to daytime hours. Train staff to avoid collecting payments during inconvenient times.
  - Provide guests with **payment schedule upon arrival** to reduce surprises.

**11: Room Comfort Issues**

  - Provide clear information about **bed sizes** in room descriptions to set guest expectations.
  - Offer **room options with larger beds** for guests needing extra comfort.
  - **Detail bed capacity** in social media posts and interactions before guest check-in. 
  - Consider upgrading or replacing smaller beds if feasible to enhance guest satisfaction.

**12: Poor WiFi Connectivity**

  - Conduct a thorough **assessment of the WiFi infrastructure** to identify **dead zones** and areas with poor signal strength.
  - **Upgrade WiFi access points** to models with better range and stability, ensuring even coverage throughout the property.
  - Regularly maintain and monitor network equipment to prevent fluctuations and outages.
  - Provide guest support and clear instructions on connecting to reliable WiFi networks.

**13: Lack of Drinking Water Facilities**

  - Install water heaters or provide **hot water dispensers** in rooms or common areas to facilitate access to hot drinking water.

**14: Room Lighting Issues**

  - **Install adjustable blackout curtains** or blinds to allow guests control over the amount of natural light.
  - Consider room orientation and window treatments during room design or renovation to minimize excessive light entry.

**15: Lack of Onsite Food Amenities**

  - Consider introducing a **cafeteria or coffee bar** to provide convenient onsite breakfast and coffee options.
  - **Promote nearby food options** clearly in the hotel information to mitigate guest inconvenience.

**16: Room Location Issues**

  - **Improve the room assignment system** to prioritize guest floor preferences during check-in.
  - Train front desk staff to verify room requests and **confirm floor allocations with guests**.
  - Update the booking system to **flag floor preferences** clearly and communicate them to housekeeping and allocation teams.
