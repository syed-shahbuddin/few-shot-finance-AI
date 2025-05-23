import requests
import os

API_KEY = os.getenv("HYPERBOLIC_API_KEY")
if not API_KEY:
    raise ValueError("API key not found. Please set the HYPERBOLIC_API_KEY environment variable.")

url = "https://api.hyperbolic.xyz/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}
data = {
    "messages": [
        {
            "role": "system",
            "content": """Here's a **few-shot prompt template** you can use to train an LLM to identify answers vs. nonanswers in earnings call transcripts:

---
 
You are a financial analyst tasked with splitting a conference call transcript into **question-answer pairs** and tagging each answer as **"answer"** (substantive, specific information) or **"nonanswer"** (vague/evasive/indirect). Use the following criteria:  

1. **Answer**: Contains quantifiable data, clear explanations, timelines, or actionable insights.  
   - Examples: "We expect Q1 sales of $17.8M, up 6% YoY," "Our market share is 60%."  
2. **Nonanswer**: Avoids specifics, deflects with generalizations, or repeats boilerplate language.  
   - Examples: "It's baked into guidance," "We're exploring all options."  

---

### **Examples**  
**Example 1**  
*Transcript Excerpt:*  
**Question:** "Are Omniflow II sales projections reflected in 2015 guidance?"  
**Answer:** "It's all baked into guidance for 2015. Q4 annualized run rate was $3.6M for Omniflow."  
**Tag:** Answer (provides run-rate data).  

**Example 2**  
*Transcript Excerpt:*  
**Question:** "Can you break down sales by geography?"  
**Answer:** "Refer to the press release for geographic sales data. The euro is the main exposure."  
**Tag:** Nonanswer (avoids specifics, redirects to external docs).  

**Example 3**  
*Transcript Excerpt:*  
**Question:** "How will R&D investments trend in 2015?"  
**Answer:** "We plan to increase R&D spending marginally this year."  
**Tag:** Nonanswer (vague, lacks numbers or timelines).  

---

### **Template for Output**  
For each question-answer pair in the transcript, format your response as:  
```  
**Question [N]**  
*Context:* [Briefly summarize inferred question topic]  
**Answer:**  
"[Exact answer text]"  
**Tag:** [Answer/Nonanswer] ([1-sentence justification]).  
```  

---

### **Input**  
<Insert new transcript here>  

---

### **Output**  
Split the transcript into question-answer pairs and apply the tagging logic from the examples.  

---

### **Additional Guidance**  
- Use context clues (e.g., "As to your question about…") to infer unspoken questions.  
- Prioritize tagging answers that include **numbers**, **dates**, or **specific strategies**.  
- Nonanswers often include phrases like "we're confident," "baked into guidance," or "we'll see."  

"""
        },
        {
            "role": "user",
            "content": """Thank you, Whitley.
Good afternoon and thank you for joining us on our Q4 2014 conference call.
Joining me on today's call is our Chairman and CEO <UNK> <UNK> and our President <UNK> <UNK>.
Before we begin, I will read our Safe Harbor statement.
Today we will make some forward-looking statements, the accuracy of which is subject to risks and uncertainties.
Wherever possible, we will try to identify those forward-looking statements by using words such as believe, expect, anticipate, forecast, and similar expressions.
Our forward-looking statements are based on our estimates and assumptions as of today, February 25, 2015, and should not be relied upon as representing our estimates or views on any subsequent date.
Please refer to the cautionary statement regarding forward-looking information and the risk factors in our most recent 10-K and subsequent SEC filings, including disclosure of the factors that could cause results to differ materially from those expressed or implied.
During this call, we will discuss non-GAAP financial measures, which include organic sales and growth numbers, as well as EBITDA.
A reconciliation of GAAP to non-GAAP measures is contained in our press release announcing the quarter's results and is available in the Investor Relations section of our website www.lemaitre.com.
I will now turn the call over to <UNK> <UNK>.
Thanks, J.
J.
Q4 2014 was a very productive quarter.
I will focus on three headlines.
First off, Q4 was a record quarter up and down the income statement.
Secondly, our recently launched HYDRO Valvulotome is performing quite well and, finally, our newly acquired Omniflow II biologic graft is performing ahead of expectations.
As to our first headline, in Q4 we posted several financial records: record sales of $18.7 million, up 4% versus Q4 2013; record EBITDA of $3.6 million, up 85%; record op income of $2.7 million, up 134%; record operating margin of 15%.
Also, net income in the quarter was $1.9 million, up 157%, and earnings were $0.11 per diluted share, up 120%.
As to our second headline, the 1.5 millimeter HYDRO Valvulotome features hydrophilic coating and a smaller diameter.
Our sales force has rallied around the HYDRO launch, and vascular surgeons have roundly praised the new device.
As part of our country by country hard switch launch, in November the HYDRO became the only <UNK> valvulotome in the US -- available in the US, excuse me.
Australia and Canada converted to the HYDRO in Q3 2014, and Europe is slated for conversion throughout 2015.
The HYDRO represented 54% of all valvulotome dollars sales in Q4.
Indeed, the launch perked up the entire valvulotome category, which grew 7.4% on a constant currency basis in Q4.
In February 2015, the valvulotome ASP in the Americas was 16% higher than in February 2014.
The HYDRO heart switch is similar to a Gillette razor upgrade.
The customer pays a premium for a noticeably improved shave.
We currently have 50% to 60% market share in valvulotomes, and we believe the HYDRO launch should increase our share.
As to our third headline, we acquired the Omniflow II biologic graft in August 2014 and spent the last four months of 2014 buying out dealers and converting to a director hospital channel.
On October 28 earnings call, we projected $3 million of Omniflow II sales in 2015.
So we were pleased to see a Q4 2014 annualized sales run rate of $3.6 million of the Omniflow II product.
We acquired Omniflow II biologic graft for three reasons.
Number one, biologic grafts are associated with less infection than standard synthetic grafts.
Number two, biologic grafts are a $30 million niche market with limited competition.
And, finally, number three, <UNK>'s 31 sales reps in Europe are a superior channel than the previous patchwork of independent distributors.
At the acquisition's six-month anniversary, our European sales force has been more enthusiastic about Omniflow II than we had expected.
Stepping back for a moment, our often stated financial objectives are fairly straightforward -- 10% annual reported sales growth and 20% annual op income growth.
For the full-year 2014, we posted 10% sales growth and 40% op income growth, and at <UNK> op income growth feeds acquisitions and dividends.
You have seen us execute four acquisitions in the last 18 months, and recently the Board approved our fourth straight annual $0.005 per share dividend increase.
Q1 2015 dividends will be $0.04 per share, a 2.1% yield.
Thanks, <UNK>.
From a bottom-line perspective, Q4 was an excellent finish to the year.
As you may recall, we posted a small operating loss in Q1 2014, executed significant cost cutting in Q1 and Q2, and over the subsequent quarters reported operating income of $2 million, $1.9 million and $2.7 million.
These results represented operating margins of 11%, 11% and 15% respectively and were driven by increased sales, as well as lower operating expenses.
Indeed, Q4 operating expenses totaled $10.1 million, a full $700,000 less than the year earlier period.
Our gross margin story in 2014 was less dramatic, and we exited the year at 68.7% in Q4.
With no new large scale integrations or disruptor product additions, over the last three quarters of the year, our gross margin hovered consistently around 68.5%.
As of late, gross margin has been characterized by several offsetting or transient items, and going forward I expect the gross margin to remain in the 68.5% range and increase marginally to 69% by Q4 of 2015.
Any analysis of sales, gross margin or operating income, however, must be viewed through the prism of recent foreign exchange swings.
As you may know, about 60% of our sales are transacted in US dollars.
In Q4 2014, we estimated that the strong dollar decreased our revenues by $670,000 and our operating income by $330,000.
Looking towards full-year 2015, we estimate that the strong dollar will decrease sales by approximately $3.7 million, reduce gross margin by 100 basis points and reduce operating income by approximately $1.8 million.
Turning to guidance, we expect Q1 2015 sales of $17.8 million, a reported increase of 6% versus Q1 2014.
Excluding the effects of changes in foreign currency exchange rates, this represents 12% sales growth.
Excluding currency effects and acquisitions, in other words organically, this represents a 7% sales growth.
We also expect Q1 2015 operating income of $1.4 million, an 8% operating margin.
For the full-year 2015, we expect sales of $74.5 million, a reported increase of 5% versus 2014.
Excluding the effects of changes in foreign currency exchange rates, this represents 10% sales growth.
Excluding currency effects and acquisitions -- in other words, organically -- this represents 6% sales growth.
We also expect full-year 2015 operating income to increase by 19% to $7.5 million, representing a 10% operating margin.
With that, I will turn it back over to the operator for Q&A.
Jason, are you out there.
Sounds like Jason is not getting to us.
Maybe he is on mute.
To the operator, this is <UNK>.
Maybe we move to the next question or see if that person also has the same problem.
Sorry about that, Jason, if you can hear us.
Yes, I think there is.
It is all baked into guidance for 2015.
You have to know that could we thought a lot about what the full guidance for revenues was going to be for 2015.
So that's already in there.
But if you want to split out mentally, yes, you are looking at at least in Q4 the annualized run rate was $3.6 million for Omniflow, and you can think of the Angioscope as unchanged from what we talked about before.
I think just because Q4 annualized at $3.6 million, I don't know necessarily if we are saying it's different in 2015, but one could follow through on that line of logic.
I see what you're saying.
Okay.
So, on the press release, in the back you can see a schedule of sales by geography, and we don't break things out anymore granular than that.
But, you know, that we are selling in those geographies from discussions with us historically in the UK, in Australia, maybe a little Norway and, so, there are some other currencies that run in and out of there and then about what you see on that grid.
But really the euro is the main piece for you.
Yes, I think we were talking about it at the Board meeting last week, and the euro was about 90% of the topic year because the euro has moved so violently.
Canadian dollar is a little bit in there as well, and then the Swiss franc obviously is going the opposite direction of those two.
But our Swiss business is only around $1 million a year, so it's not that germane.
We certainly do, and so right now, as it is constituted, we are telling you we have 81 reps on the payroll, 41 in the Americas, of which four are Canadian and the balance are American, 37, 31 in Europe, nine and Asia-Pac Rim, for a total again of 81.
I think we were talking in those terms last time, so I will continue on with that.
Usually we try not to break it out.
But I will -- I think that the total sales dollars for the year, <UNK> -- I know that's not exactly what you asked -- was about $16.5 million, including allocated shipping, and you can assume that that last quarter was a fourth of that.
I don't have better data right at my fingertips, unless anyone else on this call does.
<UNK>, you got that.
So, I would say a fourth of that, call it $4 million, $4.1 million.
23% of sales in Q4.
Yes, that's a better fact.
23% of sales exactly in Q4, <UNK>, and the sales are what, [$18.7 million].
It's a big one in 2015.
I think we've been pretty good about not advertising this.
This is not really unit growth category for us.
We're assuming flat, maybe up a little bit unit wise, but pricing wise, yes, we are thrilled to get that 16% pricing number in February in the Americas.
Largely speaking, the heart switch is all done in Australia, Canada.
The US and now Europe is all about this year.
You can think one or two countries a month for 12 months and then Japan at the end of the year.
So, yes, and in answer to your question, yes, big growth driver.
Of course, XenoSure we expect to continue to be a large growth driver and then also Omniflow.
We talked about that.
We know that we booked exactly $1 million of revenue in Omniflow in 2014, and we just were talking through what is the guidance for 2015.
Maybe it's $3.5 million as the previous gentlemen was discussing, so maybe that growth is [$2.5] from 2014 to 2015 for Omniflow, and then you got XenoSure and the valvulotome, and those are the big guys for growth.
Sure.
We didn't -- during the quarter, at the last call, we also had 81, <UNK>, but your broader point is correct, which is when we came to talk to you guys in April, we had 87 reps on the payroll, and now we have 81 at this juncture.
So seven are down, and it's actually four of them come out of Europe, one out of the Pac Rim and one out of the Americas.
And then in final answer to your question, yes, we do plan to replace them.
We are talking about 89, 90 reps by the end of the year, and we feel like the organic growth can get scooched up.
We had a 6% organic growth for 2014, and we feel like we can do a little better with a little bit of rep growth.
I would say, <UNK>, first of all, you are correct.
We have been in the 6.3% range the last couple of quarters.
Now you are in the 5.8% range, and I would take that going forward we want to see that go higher.
I think we would want to invest a little bit more in R&D, and we will probably work to do that over the coming year.
You can see us a year ago in the high 7s% range, 8% range and, so, we would probably try and work to get at least partially back there as the year goes on.
Yes, so there's a lot of offsets in gross margin going back and forth.
Some of the higher level ones are with the [B&I] acquisition, there was a inventory writeup for purchase price accounting that is going to go away.
So we're going to have some accounting help there.
I think also on the XenoSure manufacturing line, we're going to see some improvement there as we drive XenoSure costs down, and that will flow through the gross margin as the year goes on.
And, certainly, since Q4 from 2014 to 2015 through the year, we will have ASP increases that will help as well.
So, I think those are the good guys going through gross margin, <UNK>, and then some of the offsets might be mix and certainly FX.
Okay, sure, yes.
<UNK>, I would say as you look at the last couple of years, do remember that at the very end of Q3 in both 2013 and 2014 we bought sizable companies, which then artificially, if you will, pumped up Q4 revenue, so just keep that in mind.
But in general, the pattern for us as we look at revenues is quite clear, which is Q1 is always a light quarter, and Q3 is always a light quarter.
Q2 is really good, and then Q4 winds up being a record, if you will, inside of those four quarters.
So, Q2 and Q4 are the biggies, and then because we are such a European business in Q3, it is light in the summer, and Q1 I think you are recovering from the end of the year where the sales reps are all rallying to get to their numbers.
Interesting, we didn't break that out as we were giving you this number, so we don't have a breakdown.
We have budgets.
I would say you can feel pretty confident that our international business is running really well right now, and, so, I would say at a very high level, the lion's share of that growth is coming out of international.
In particular, Europe just continues to excel even our expectations.
So, I would say it is a European number with the US bringing it down a bit.
Yes, I would say we obviously have completed the transition quote-unquote and gained some good stability a number of quarters back in XenoSure manufacturing, and now it's about squeezing costs out of that room.
And I think that's already started, and it started as part of the cost-cutting efforts last year, and it will continue through this year.
So I'm going to say, if you think about it, in a little bit of a linear fashion throughout this year and then maybe it starts tailing off in subsequent years, but I think you're going to get some decent traction this year.
Sure thing, <UNK>.
It's <UNK>.
I would say we have been -- I've been busy restocking the pipeline since the couple a deals in Q3, and obviously we have been focused a lot around (inaudible) integration.
We have a good number of targets.
The criteria has not changed.
In general, I would say they are a little bit larger than what we have looked at in the past.
So, just doing what we do, waiting for our pitch and trying to find the right target to swing at.
Right.
<UNK>, your question -- this is <UNK> -- your question, your voice cut out right at the meat of your question.
I think you are asking about us redoing the sales force back up to 90.
I'm going to answer like that.
So, the great thing, the exciting thing about <UNK> right now is that we have access to so many countries, so we get to really look at what are the best cities to go into, and, so, for us, you're going to see places, we think, this year like Shanghai, like Beijing, like Auckland, a couple in Europe.
I can name Rotterdam and Stuttgart and then us fill in in the US with four or five.
So, it will sprinkle around the world.
I think the bigger opportunities are Asia-Pac Rim and then filling in Europe because we have so many great products over there that have all the approvals over there, and in the US we don't quite have as many devices because it is a little bit more difficult to get some of these products approved in the US.
So, a sprinkling all around the world getting up to 90.
I hope that answers your question.
That's a great question, <UNK>.
I hadn't really thought about it that way, but I do think we do want to stay to this goal of, hey, we're going to try to grow revenue for you 10%, and I do feel like the organic numbers for the last few -- put the last six years together, they come out at 7%.
So I do think the management team does feel some kick in the behind that we need to buy stuff.
We need to set up distribution relationships with this.
I think we have been pretty selective and judicious.
I think you are saying that in your question.
I don't think we will do anything dumb, but I do feel some pressure to go out and deploy the capital.
We have $18 million of cash on the balance sheet.
We expect, we're not really guiding on cash, but we expect to be fairly cash flow positive here.
And so it's got to go somewhere.
It is going into dividends and acquisitions, so we do feel like we're an acquisitive company, and we take pride in that, and we want to keep pushing on that.
I hope that answers my question.
<UNK>, you got a different -- slightly different angle on that or --.
I would just add that acquisitions certainly give us size and critical mass and give us leverage, and the way this business model works is we get bigger.
We add more reps, more infrastructure, and we get stronger.
And, so, yes, acquisitions, it has been a fundamental part of the business plan for 17 years.
It will continue to be.
But, as everybody knows who watches <UNK>, we're deliberate.
We are never desperate.
We are somewhat price sensitive.
We will wait for our pitch, but if we see the right target, we will execute on it.
<UNK>, I hope that gets to your question from two angles.
That's interesting.
I'm going to say I don't have to deal with that topic right now, because it's not in front of me, but that's an interesting topic, <UNK>.
I can't answer that.
It seems so hypothetical out there.
Right now I do think as we try to transmit to Wall Street what our capital allocation strategy is, I think we are aggressively pursuing acquisitions and dividends.
So, <UNK>, this is <UNK>.
Thanks for the great question.
Terrific question.
I do notice that you are cherry picking off my best op margin of the history of time of 15%, and then you're going from there and I appreciate that.
I would say just to temper this all, we saw this coming three quarters ago.
We do still feel like the year was a 9% op margin year, and our guidance is telling you that we are 10% next year.
Definitely, you can hear through <UNK>'s comments about acquisitions, we feel strongly that if we can get bigger, we can really start pulling operating leverage out of this business, and I think for the first time since we have been doing this, remember we had three straight years of $4 million in op income, and we have finally broken out of that to the $6.3 million number.
So, we are starting to show op leverage, and I think you are right on, when we get bigger, we feel like we can do better than a 10%, but I hesitate to guide up to what we can get to.
We do know from this year in Q2 11%, Q3 11%, and Q4 15%.
We do know that these numbers are possible at <UNK>, although I think you can hear on some of these questions about sales reps and R&D, we probably need to tweak in a little bit more investment into the sales force and R&D, which might take you down a little bit from 15%.
I hope that gets to part of your question.
Maybe J.
can take it more from a CFO perspective.
Yes, so, <UNK>, if you think of us as a 8%, 9%, 10% op margin company, because that's annually where we have been as opposed to 15% of the last quarter, and then you think as we grow where we are going to get leverage, you can probably go to selling and marketing as we fill out existing geographies and cover fixed costs in those existing geographies, and maybe you can get a few points there or a couple points, and then G&A you don't need another CFO or CEO, and you're going to get some points there.
And R&D, as <UNK> said, probably not want to continue to investment spend there, and then maybe even get a little bit in gross margin as time goes on.
So, you can probably tally those us and think that maybe there is some blue sky out there potentially, and we're certainly not guiding that as you get larger in scale, you can get some better percent, lower percentage of sales numbers in those areas.
Yes, absolutely, and as <UNK> was getting at, it is driving our desire to have a larger company, which pushes us to do acquisitions, because of what you're after, which is op margin and leverage.
Yes, so, the XenoSure piece we haven't really quantified for you.
I would say improvements are baked into guidance.
So, as you get from the 68.5% to 69% over the course of the year, that's a piece of it.
You may get some decent improvement in the product line itself, but remember it is some fraction of the total sales pie.
So it's not going to be the driver of gross margin improvement, but it will have a marginal impact.
Sorry, I didn't answer your question directly.
As it relates to Asia, we have filed in Australia, feels like it's about 12 months, 18 months away.
We filed in China.
It feels like it's about 24 months away, and this isn't quite Asia but Russia we just filed, and then specifically on Japan, which is probably what you're getting at as well, we still have not committed to what is almost certainly a three-year-ish clinical trial with $1 million or so in expenses.
So we are still sorting out what we should do in Japan, but certainly China and Australia we are chasing down.
So, just to -- I hate to micromanage that question, but we are talking about 10% reported revenue growth, not organic growth.
But I know you still have the question about are there other places where we want to get growth through pricing and, yes, we do.
So we didn't talk much about our pipeline of new products today, but we do -- we got a first-in-man for what we call the long AnastoClip, and that's happening in Q2, and we think we're going to do first-in-man for our shunt flow monitor project, and I would say on that second project that's a $10 million category for <UNK>, and is largely an American product line where price flexibility is the highest at the hospital level.
And, so, I think to your question, I think what you are seeing us try to do with the valvulotome, make a big change and then get a price hike back for that, I think you're going to see us try to do on another one of our, call it, mega categories, which is the shunt business, when that thing gets rolling, my guess is you don't see any impact, material impact from that project until 2016 and maybe even into 2017.
But, yes, we are going after that, and it's our third or fourth largest product line."""
        }
    ],
    "model": "deepseek-ai/DeepSeek-V3",
    "max_tokens": 4046,
    "temperature": 0.1,
    "top_p": 0.9
}
  
response = requests.post(url, headers=headers, json=data)
response_json = response.json()

try:
    content = response_json['choices'][0]['message']['content']
    print("\nExtracted content:")
    print(content)
except KeyError as e:
    print("Error: Unexpected response format.")
    # Optionally log the error somewhere secure, but don't print sensitive info