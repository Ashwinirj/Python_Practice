def winner(erica, bob) {

#    Write your code here

  const getScore = (str) => {

    let scoreMap = {

      E: 1,

      M: 3,

      H: 5

    }

    let score = 0;

    str.split("").forEach(el => {

      if(el){

        score = score + scoreMap[el];

      }

    });

    return score;

  };

   let sEri = getScore(erica);

   let sBob = getScore(bob);

  if(sEri > sBob ){

    return "Erica";

  }

  else if(sEri < sBob){

    return "Bob";

  }

  return "Tie";

}