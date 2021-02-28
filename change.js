const tip1 = `<p class="important-text">Buy foods locally and in season<p/> - buying foods locally reduces the carbon foot print associated with transportation. Buying foods in seasons also reduces the carbon footprint as this reduces the need for intensive farming methods and packaging to store the food.`;
const tip2 = `<p class="important-text">Reduce food waste<p/> - One third of all food produced is wasted, representing 14 million tonnes of carbon dioxide emissions in the UK (equivalent to the CO2 produced by 7 million cars each year!)`;
const tip3 = `<p class="important-text">Home-cooked food</p> - this reduces footprint compared to eating in a restaurant. Remember to try to buy food that uses less packaging! Choose your food wisely; meat and dairy are associated with much higher carbon emissions than plant-based food.`;
const tips = [tip1, tip2, tip3];
var tip = document.getElementById("tip")

function change(i) {
    tip.innerHTML = tips[i-1];
}