#/bin/bash

export STANFORD_NLP_HOME=D:/users/v-qizhou/Projects/stanford-corenlp-full-2016-10-31
export GIGAHOME=D:/users/v-qizhou/Data/LDC2011T07_EngGigaword5th/Data/LDC2011T07_Original
export OUTDIR=D:/users/v-qizhou/Data/LDC2011T07_EngGigaword5th/Data/LDC2011T07_Original/extracted
export FINAL_OUTPUTDIR=D:/users/v-qizhou/Data/LDC2011T07_EngGigaword5th/Data/LDC2011T07_Original/processed
export SCRIPTHOME=D:/users/v-qizhou/Projects/NAMAS/dataset
export THREADS=10


#echo "Step 1: Construct the title-article pairs from gigaword"
#mkdir -p $OUTDIR
#find $GIGAHOME/data/???_???/*.gz | xargs -P $THREADS -I {} bash -c 'python $SCRIPTHOME/process_giga.py {} $OUTDIR'
#
#
#echo "Step 2: Split the data into train/dev/test."
#cd $OUTDIR
#cat $SCRIPTHOME/train.splits | xargs -I {} bash -c 'cat {} >> $OUTDIR/train.data.txt'
#cat $SCRIPTHOME/valid.splits | xargs -I {} bash -c 'cat {} >> $OUTDIR/valid.data.txt'
#cat $SCRIPTHOME/test.splits  | xargs -I {} bash -c 'cat {} >> $OUTDIR/test.data.txt'
#
#
#echo "Step 3: Split to title-article files and tokenize."
#python $SCRIPTHOME/my_cut.py $OUTDIR/train.data.txt
#python $SCRIPTHOME/my_cut.py $OUTDIR/valid.data.txt
#python $SCRIPTHOME/my_cut.py $OUTDIR/test.data.txt
#
#java -cp "$STANFORD_NLP_HOME/*" edu.stanford.nlp.process.PTBTokenizer -preserveLines -options "strictTreebank3=true,untokenizable=allKeep,ptb3Escaping=true" $OUTDIR/train.data.txt.article > $OUTDIR/train.data.txt.article.tok
#java -cp "$STANFORD_NLP_HOME/*" edu.stanford.nlp.process.PTBTokenizer -preserveLines -options "strictTreebank3=true,untokenizable=allKeep,ptb3Escaping=true" $OUTDIR/train.data.txt.title > $OUTDIR/train.data.txt.title.tok
#java -cp "$STANFORD_NLP_HOME/*" edu.stanford.nlp.process.PTBTokenizer -preserveLines -options "strictTreebank3=true,untokenizable=allKeep,ptb3Escaping=true" $OUTDIR/valid.data.txt.article > $OUTDIR/valid.data.txt.article.tok
#java -cp "$STANFORD_NLP_HOME/*" edu.stanford.nlp.process.PTBTokenizer -preserveLines -options "strictTreebank3=true,untokenizable=allKeep,ptb3Escaping=true" $OUTDIR/valid.data.txt.title > $OUTDIR/valid.data.txt.title.tok
#java -cp "$STANFORD_NLP_HOME/*" edu.stanford.nlp.process.PTBTokenizer -preserveLines -options "strictTreebank3=true,untokenizable=allKeep,ptb3Escaping=true" $OUTDIR/test.data.txt.article > $OUTDIR/test.data.txt.article.tok
#java -cp "$STANFORD_NLP_HOME/*" edu.stanford.nlp.process.PTBTokenizer -preserveLines -options "strictTreebank3=true,untokenizable=allKeep,ptb3Escaping=true" $OUTDIR/test.data.txt.title > $OUTDIR/test.data.txt.title.tok

echo "Step 4: Basic filtering on train/dev/test."
python $SCRIPTHOME/filter.py $OUTDIR/train.data.txt.article.tok $OUTDIR/train.data.txt.title.tok
python $SCRIPTHOME/filter.py $OUTDIR/valid.data.txt.article.tok $OUTDIR/valid.data.txt.title.tok
python $SCRIPTHOME/filter.py $OUTDIR/test.data.txt.article.tok $OUTDIR/test.data.txt.title.tok

mv $OUTDIR/train.data.txt.article.tok.filter $FINAL_OUTPUTDIR/train.data.txt.article.tok.filter
mv $OUTDIR/train.data.txt.title.tok.filter $FINAL_OUTPUTDIR/train.data.txt.title.tok.filter
mv $OUTDIR/valid.data.txt.article.tok.filter $FINAL_OUTPUTDIR/valid.data.txt.article.tok.filter
mv $OUTDIR/valid.data.txt.title.tok.filter $FINAL_OUTPUTDIR/valid.data.txt.title.tok.filter
mv $OUTDIR/test.data.txt.article.tok.filter $FINAL_OUTPUTDIR/test.data.txt.article.tok.filter
mv $OUTDIR/test.data.txt.title.tok.filter $FINAL_OUTPUTDIR/test.data.txt.title.tok.filter

